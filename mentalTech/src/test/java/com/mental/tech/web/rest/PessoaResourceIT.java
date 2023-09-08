package com.mental.tech.web.rest;

import static org.assertj.core.api.Assertions.assertThat;
import static org.hamcrest.Matchers.hasItem;
import static org.hamcrest.Matchers.is;

import com.mental.tech.IntegrationTest;
import com.mental.tech.domain.Pessoa;
import com.mental.tech.domain.enumeration.sexoEnum;
import com.mental.tech.repository.EntityManager;
import com.mental.tech.repository.PessoaRepository;
import com.mental.tech.service.dto.PessoaDTO;
import com.mental.tech.service.mapper.PessoaMapper;
import java.time.LocalDate;
import java.time.ZoneId;
import java.util.List;
import java.util.Random;
import java.util.concurrent.atomic.AtomicLong;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.reactive.AutoConfigureWebTestClient;
import org.springframework.http.MediaType;
import org.springframework.security.test.context.support.WithMockUser;
import org.springframework.test.web.reactive.server.WebTestClient;

/**
 * Integration tests for the {@link PessoaResource} REST controller.
 */
@IntegrationTest
@AutoConfigureWebTestClient(timeout = IntegrationTest.DEFAULT_ENTITY_TIMEOUT)
@WithMockUser
class PessoaResourceIT {

    private static final Integer DEFAULT_ID_PESSOA = 1;
    private static final Integer UPDATED_ID_PESSOA = 2;
    private static final Integer SMALLER_ID_PESSOA = 1 - 1;

    private static final String DEFAULT_NOME = "AAAAAAAAAA";
    private static final String UPDATED_NOME = "BBBBBBBBBB";

    private static final LocalDate DEFAULT_DATA_NASCIMENTO = LocalDate.ofEpochDay(0L);
    private static final LocalDate UPDATED_DATA_NASCIMENTO = LocalDate.now(ZoneId.systemDefault());
    private static final LocalDate SMALLER_DATA_NASCIMENTO = LocalDate.ofEpochDay(-1L);

    private static final String DEFAULT_EMAIL = "AAAAAAAAAA";
    private static final String UPDATED_EMAIL = "BBBBBBBBBB";

    private static final sexoEnum DEFAULT_SEXO = sexoEnum.F;
    private static final sexoEnum UPDATED_SEXO = sexoEnum.M;

    private static final Integer DEFAULT_TELEFONE = 15;
    private static final Integer UPDATED_TELEFONE = 14;
    private static final Integer SMALLER_TELEFONE = 15 - 1;

    private static final String DEFAULT_SENHA = "AAAAAAAAAA";
    private static final String UPDATED_SENHA = "BBBBBBBBBB";

    private static final String ENTITY_API_URL = "/api/pessoas";
    private static final String ENTITY_API_URL_ID = ENTITY_API_URL + "/{id}";

    private static Random random = new Random();
    private static AtomicLong count = new AtomicLong(random.nextInt() + (2 * Integer.MAX_VALUE));

    @Autowired
    private PessoaRepository pessoaRepository;

    @Autowired
    private PessoaMapper pessoaMapper;

    @Autowired
    private EntityManager em;

    @Autowired
    private WebTestClient webTestClient;

    private Pessoa pessoa;

    /**
     * Create an entity for this test.
     *
     * This is a static method, as tests for other entities might also need it,
     * if they test an entity which requires the current entity.
     */
    public static Pessoa createEntity(EntityManager em) {
        Pessoa pessoa = new Pessoa()
            .idPessoa(DEFAULT_ID_PESSOA)
            .nome(DEFAULT_NOME)
            .dataNascimento(DEFAULT_DATA_NASCIMENTO)
            .email(DEFAULT_EMAIL)
            .sexo(DEFAULT_SEXO)
            .telefone(DEFAULT_TELEFONE)
            .senha(DEFAULT_SENHA);
        return pessoa;
    }

    /**
     * Create an updated entity for this test.
     *
     * This is a static method, as tests for other entities might also need it,
     * if they test an entity which requires the current entity.
     */
    public static Pessoa createUpdatedEntity(EntityManager em) {
        Pessoa pessoa = new Pessoa()
            .idPessoa(UPDATED_ID_PESSOA)
            .nome(UPDATED_NOME)
            .dataNascimento(UPDATED_DATA_NASCIMENTO)
            .email(UPDATED_EMAIL)
            .sexo(UPDATED_SEXO)
            .telefone(UPDATED_TELEFONE)
            .senha(UPDATED_SENHA);
        return pessoa;
    }

    public static void deleteEntities(EntityManager em) {
        try {
            em.deleteAll(Pessoa.class).block();
        } catch (Exception e) {
            // It can fail, if other entities are still referring this - it will be removed later.
        }
    }

    @AfterEach
    public void cleanup() {
        deleteEntities(em);
    }

    @BeforeEach
    public void initTest() {
        deleteEntities(em);
        pessoa = createEntity(em);
    }

    @Test
    void createPessoa() throws Exception {
        int databaseSizeBeforeCreate = pessoaRepository.findAll().collectList().block().size();
        // Create the Pessoa
        PessoaDTO pessoaDTO = pessoaMapper.toDto(pessoa);
        webTestClient
            .post()
            .uri(ENTITY_API_URL)
            .contentType(MediaType.APPLICATION_JSON)
            .bodyValue(TestUtil.convertObjectToJsonBytes(pessoaDTO))
            .exchange()
            .expectStatus()
            .isCreated();

        // Validate the Pessoa in the database
        List<Pessoa> pessoaList = pessoaRepository.findAll().collectList().block();
        assertThat(pessoaList).hasSize(databaseSizeBeforeCreate + 1);
        Pessoa testPessoa = pessoaList.get(pessoaList.size() - 1);
        assertThat(testPessoa.getIdPessoa()).isEqualTo(DEFAULT_ID_PESSOA);
        assertThat(testPessoa.getNome()).isEqualTo(DEFAULT_NOME);
        assertThat(testPessoa.getDataNascimento()).isEqualTo(DEFAULT_DATA_NASCIMENTO);
        assertThat(testPessoa.getEmail()).isEqualTo(DEFAULT_EMAIL);
        assertThat(testPessoa.getSexo()).isEqualTo(DEFAULT_SEXO);
        assertThat(testPessoa.getTelefone()).isEqualTo(DEFAULT_TELEFONE);
        assertThat(testPessoa.getSenha()).isEqualTo(DEFAULT_SENHA);
    }

    @Test
    void createPessoaWithExistingId() throws Exception {
        // Create the Pessoa with an existing ID
        pessoa.setId(1L);
        PessoaDTO pessoaDTO = pessoaMapper.toDto(pessoa);

        int databaseSizeBeforeCreate = pessoaRepository.findAll().collectList().block().size();

        // An entity with an existing ID cannot be created, so this API call must fail
        webTestClient
            .post()
            .uri(ENTITY_API_URL)
            .contentType(MediaType.APPLICATION_JSON)
            .bodyValue(TestUtil.convertObjectToJsonBytes(pessoaDTO))
            .exchange()
            .expectStatus()
            .isBadRequest();

        // Validate the Pessoa in the database
        List<Pessoa> pessoaList = pessoaRepository.findAll().collectList().block();
        assertThat(pessoaList).hasSize(databaseSizeBeforeCreate);
    }

    @Test
    void checkIdPessoaIsRequired() throws Exception {
        int databaseSizeBeforeTest = pessoaRepository.findAll().collectList().block().size();
        // set the field null
        pessoa.setIdPessoa(null);

        // Create the Pessoa, which fails.
        PessoaDTO pessoaDTO = pessoaMapper.toDto(pessoa);

        webTestClient
            .post()
            .uri(ENTITY_API_URL)
            .contentType(MediaType.APPLICATION_JSON)
            .bodyValue(TestUtil.convertObjectToJsonBytes(pessoaDTO))
            .exchange()
            .expectStatus()
            .isBadRequest();

        List<Pessoa> pessoaList = pessoaRepository.findAll().collectList().block();
        assertThat(pessoaList).hasSize(databaseSizeBeforeTest);
    }

    @Test
    void checkDataNascimentoIsRequired() throws Exception {
        int databaseSizeBeforeTest = pessoaRepository.findAll().collectList().block().size();
        // set the field null
        pessoa.setDataNascimento(null);

        // Create the Pessoa, which fails.
        PessoaDTO pessoaDTO = pessoaMapper.toDto(pessoa);

        webTestClient
            .post()
            .uri(ENTITY_API_URL)
            .contentType(MediaType.APPLICATION_JSON)
            .bodyValue(TestUtil.convertObjectToJsonBytes(pessoaDTO))
            .exchange()
            .expectStatus()
            .isBadRequest();

        List<Pessoa> pessoaList = pessoaRepository.findAll().collectList().block();
        assertThat(pessoaList).hasSize(databaseSizeBeforeTest);
    }

    @Test
    void checkEmailIsRequired() throws Exception {
        int databaseSizeBeforeTest = pessoaRepository.findAll().collectList().block().size();
        // set the field null
        pessoa.setEmail(null);

        // Create the Pessoa, which fails.
        PessoaDTO pessoaDTO = pessoaMapper.toDto(pessoa);

        webTestClient
            .post()
            .uri(ENTITY_API_URL)
            .contentType(MediaType.APPLICATION_JSON)
            .bodyValue(TestUtil.convertObjectToJsonBytes(pessoaDTO))
            .exchange()
            .expectStatus()
            .isBadRequest();

        List<Pessoa> pessoaList = pessoaRepository.findAll().collectList().block();
        assertThat(pessoaList).hasSize(databaseSizeBeforeTest);
    }

    @Test
    void checkSexoIsRequired() throws Exception {
        int databaseSizeBeforeTest = pessoaRepository.findAll().collectList().block().size();
        // set the field null
        pessoa.setSexo(null);

        // Create the Pessoa, which fails.
        PessoaDTO pessoaDTO = pessoaMapper.toDto(pessoa);

        webTestClient
            .post()
            .uri(ENTITY_API_URL)
            .contentType(MediaType.APPLICATION_JSON)
            .bodyValue(TestUtil.convertObjectToJsonBytes(pessoaDTO))
            .exchange()
            .expectStatus()
            .isBadRequest();

        List<Pessoa> pessoaList = pessoaRepository.findAll().collectList().block();
        assertThat(pessoaList).hasSize(databaseSizeBeforeTest);
    }

    @Test
    void getAllPessoas() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList
        webTestClient
            .get()
            .uri(ENTITY_API_URL + "?sort=id,desc")
            .accept(MediaType.APPLICATION_JSON)
            .exchange()
            .expectStatus()
            .isOk()
            .expectHeader()
            .contentType(MediaType.APPLICATION_JSON)
            .expectBody()
            .jsonPath("$.[*].id")
            .value(hasItem(pessoa.getId().intValue()))
            .jsonPath("$.[*].idPessoa")
            .value(hasItem(DEFAULT_ID_PESSOA))
            .jsonPath("$.[*].nome")
            .value(hasItem(DEFAULT_NOME))
            .jsonPath("$.[*].dataNascimento")
            .value(hasItem(DEFAULT_DATA_NASCIMENTO.toString()))
            .jsonPath("$.[*].email")
            .value(hasItem(DEFAULT_EMAIL))
            .jsonPath("$.[*].sexo")
            .value(hasItem(DEFAULT_SEXO.toString()))
            .jsonPath("$.[*].telefone")
            .value(hasItem(DEFAULT_TELEFONE))
            .jsonPath("$.[*].senha")
            .value(hasItem(DEFAULT_SENHA));
    }

    @Test
    void getPessoa() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get the pessoa
        webTestClient
            .get()
            .uri(ENTITY_API_URL_ID, pessoa.getId())
            .accept(MediaType.APPLICATION_JSON)
            .exchange()
            .expectStatus()
            .isOk()
            .expectHeader()
            .contentType(MediaType.APPLICATION_JSON)
            .expectBody()
            .jsonPath("$.id")
            .value(is(pessoa.getId().intValue()))
            .jsonPath("$.idPessoa")
            .value(is(DEFAULT_ID_PESSOA))
            .jsonPath("$.nome")
            .value(is(DEFAULT_NOME))
            .jsonPath("$.dataNascimento")
            .value(is(DEFAULT_DATA_NASCIMENTO.toString()))
            .jsonPath("$.email")
            .value(is(DEFAULT_EMAIL))
            .jsonPath("$.sexo")
            .value(is(DEFAULT_SEXO.toString()))
            .jsonPath("$.telefone")
            .value(is(DEFAULT_TELEFONE))
            .jsonPath("$.senha")
            .value(is(DEFAULT_SENHA));
    }

    @Test
    void getPessoasByIdFiltering() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        Long id = pessoa.getId();

        defaultPessoaShouldBeFound("id.equals=" + id);
        defaultPessoaShouldNotBeFound("id.notEquals=" + id);

        defaultPessoaShouldBeFound("id.greaterThanOrEqual=" + id);
        defaultPessoaShouldNotBeFound("id.greaterThan=" + id);

        defaultPessoaShouldBeFound("id.lessThanOrEqual=" + id);
        defaultPessoaShouldNotBeFound("id.lessThan=" + id);
    }

    @Test
    void getAllPessoasByIdPessoaIsEqualToSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where idPessoa equals to DEFAULT_ID_PESSOA
        defaultPessoaShouldBeFound("idPessoa.equals=" + DEFAULT_ID_PESSOA);

        // Get all the pessoaList where idPessoa equals to UPDATED_ID_PESSOA
        defaultPessoaShouldNotBeFound("idPessoa.equals=" + UPDATED_ID_PESSOA);
    }

    @Test
    void getAllPessoasByIdPessoaIsInShouldWork() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where idPessoa in DEFAULT_ID_PESSOA or UPDATED_ID_PESSOA
        defaultPessoaShouldBeFound("idPessoa.in=" + DEFAULT_ID_PESSOA + "," + UPDATED_ID_PESSOA);

        // Get all the pessoaList where idPessoa equals to UPDATED_ID_PESSOA
        defaultPessoaShouldNotBeFound("idPessoa.in=" + UPDATED_ID_PESSOA);
    }

    @Test
    void getAllPessoasByIdPessoaIsNullOrNotNull() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where idPessoa is not null
        defaultPessoaShouldBeFound("idPessoa.specified=true");

        // Get all the pessoaList where idPessoa is null
        defaultPessoaShouldNotBeFound("idPessoa.specified=false");
    }

    @Test
    void getAllPessoasByIdPessoaIsGreaterThanOrEqualToSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where idPessoa is greater than or equal to DEFAULT_ID_PESSOA
        defaultPessoaShouldBeFound("idPessoa.greaterThanOrEqual=" + DEFAULT_ID_PESSOA);

        // Get all the pessoaList where idPessoa is greater than or equal to UPDATED_ID_PESSOA
        defaultPessoaShouldNotBeFound("idPessoa.greaterThanOrEqual=" + UPDATED_ID_PESSOA);
    }

    @Test
    void getAllPessoasByIdPessoaIsLessThanOrEqualToSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where idPessoa is less than or equal to DEFAULT_ID_PESSOA
        defaultPessoaShouldBeFound("idPessoa.lessThanOrEqual=" + DEFAULT_ID_PESSOA);

        // Get all the pessoaList where idPessoa is less than or equal to SMALLER_ID_PESSOA
        defaultPessoaShouldNotBeFound("idPessoa.lessThanOrEqual=" + SMALLER_ID_PESSOA);
    }

    @Test
    void getAllPessoasByIdPessoaIsLessThanSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where idPessoa is less than DEFAULT_ID_PESSOA
        defaultPessoaShouldNotBeFound("idPessoa.lessThan=" + DEFAULT_ID_PESSOA);

        // Get all the pessoaList where idPessoa is less than UPDATED_ID_PESSOA
        defaultPessoaShouldBeFound("idPessoa.lessThan=" + UPDATED_ID_PESSOA);
    }

    @Test
    void getAllPessoasByIdPessoaIsGreaterThanSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where idPessoa is greater than DEFAULT_ID_PESSOA
        defaultPessoaShouldNotBeFound("idPessoa.greaterThan=" + DEFAULT_ID_PESSOA);

        // Get all the pessoaList where idPessoa is greater than SMALLER_ID_PESSOA
        defaultPessoaShouldBeFound("idPessoa.greaterThan=" + SMALLER_ID_PESSOA);
    }

    @Test
    void getAllPessoasByNomeIsEqualToSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where nome equals to DEFAULT_NOME
        defaultPessoaShouldBeFound("nome.equals=" + DEFAULT_NOME);

        // Get all the pessoaList where nome equals to UPDATED_NOME
        defaultPessoaShouldNotBeFound("nome.equals=" + UPDATED_NOME);
    }

    @Test
    void getAllPessoasByNomeIsInShouldWork() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where nome in DEFAULT_NOME or UPDATED_NOME
        defaultPessoaShouldBeFound("nome.in=" + DEFAULT_NOME + "," + UPDATED_NOME);

        // Get all the pessoaList where nome equals to UPDATED_NOME
        defaultPessoaShouldNotBeFound("nome.in=" + UPDATED_NOME);
    }

    @Test
    void getAllPessoasByNomeIsNullOrNotNull() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where nome is not null
        defaultPessoaShouldBeFound("nome.specified=true");

        // Get all the pessoaList where nome is null
        defaultPessoaShouldNotBeFound("nome.specified=false");
    }

    @Test
    void getAllPessoasByNomeContainsSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where nome contains DEFAULT_NOME
        defaultPessoaShouldBeFound("nome.contains=" + DEFAULT_NOME);

        // Get all the pessoaList where nome contains UPDATED_NOME
        defaultPessoaShouldNotBeFound("nome.contains=" + UPDATED_NOME);
    }

    @Test
    void getAllPessoasByNomeNotContainsSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where nome does not contain DEFAULT_NOME
        defaultPessoaShouldNotBeFound("nome.doesNotContain=" + DEFAULT_NOME);

        // Get all the pessoaList where nome does not contain UPDATED_NOME
        defaultPessoaShouldBeFound("nome.doesNotContain=" + UPDATED_NOME);
    }

    @Test
    void getAllPessoasByDataNascimentoIsEqualToSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where dataNascimento equals to DEFAULT_DATA_NASCIMENTO
        defaultPessoaShouldBeFound("dataNascimento.equals=" + DEFAULT_DATA_NASCIMENTO);

        // Get all the pessoaList where dataNascimento equals to UPDATED_DATA_NASCIMENTO
        defaultPessoaShouldNotBeFound("dataNascimento.equals=" + UPDATED_DATA_NASCIMENTO);
    }

    @Test
    void getAllPessoasByDataNascimentoIsInShouldWork() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where dataNascimento in DEFAULT_DATA_NASCIMENTO or UPDATED_DATA_NASCIMENTO
        defaultPessoaShouldBeFound("dataNascimento.in=" + DEFAULT_DATA_NASCIMENTO + "," + UPDATED_DATA_NASCIMENTO);

        // Get all the pessoaList where dataNascimento equals to UPDATED_DATA_NASCIMENTO
        defaultPessoaShouldNotBeFound("dataNascimento.in=" + UPDATED_DATA_NASCIMENTO);
    }

    @Test
    void getAllPessoasByDataNascimentoIsNullOrNotNull() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where dataNascimento is not null
        defaultPessoaShouldBeFound("dataNascimento.specified=true");

        // Get all the pessoaList where dataNascimento is null
        defaultPessoaShouldNotBeFound("dataNascimento.specified=false");
    }

    @Test
    void getAllPessoasByDataNascimentoIsGreaterThanOrEqualToSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where dataNascimento is greater than or equal to DEFAULT_DATA_NASCIMENTO
        defaultPessoaShouldBeFound("dataNascimento.greaterThanOrEqual=" + DEFAULT_DATA_NASCIMENTO);

        // Get all the pessoaList where dataNascimento is greater than or equal to UPDATED_DATA_NASCIMENTO
        defaultPessoaShouldNotBeFound("dataNascimento.greaterThanOrEqual=" + UPDATED_DATA_NASCIMENTO);
    }

    @Test
    void getAllPessoasByDataNascimentoIsLessThanOrEqualToSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where dataNascimento is less than or equal to DEFAULT_DATA_NASCIMENTO
        defaultPessoaShouldBeFound("dataNascimento.lessThanOrEqual=" + DEFAULT_DATA_NASCIMENTO);

        // Get all the pessoaList where dataNascimento is less than or equal to SMALLER_DATA_NASCIMENTO
        defaultPessoaShouldNotBeFound("dataNascimento.lessThanOrEqual=" + SMALLER_DATA_NASCIMENTO);
    }

    @Test
    void getAllPessoasByDataNascimentoIsLessThanSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where dataNascimento is less than DEFAULT_DATA_NASCIMENTO
        defaultPessoaShouldNotBeFound("dataNascimento.lessThan=" + DEFAULT_DATA_NASCIMENTO);

        // Get all the pessoaList where dataNascimento is less than UPDATED_DATA_NASCIMENTO
        defaultPessoaShouldBeFound("dataNascimento.lessThan=" + UPDATED_DATA_NASCIMENTO);
    }

    @Test
    void getAllPessoasByDataNascimentoIsGreaterThanSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where dataNascimento is greater than DEFAULT_DATA_NASCIMENTO
        defaultPessoaShouldNotBeFound("dataNascimento.greaterThan=" + DEFAULT_DATA_NASCIMENTO);

        // Get all the pessoaList where dataNascimento is greater than SMALLER_DATA_NASCIMENTO
        defaultPessoaShouldBeFound("dataNascimento.greaterThan=" + SMALLER_DATA_NASCIMENTO);
    }

    @Test
    void getAllPessoasByEmailIsEqualToSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where email equals to DEFAULT_EMAIL
        defaultPessoaShouldBeFound("email.equals=" + DEFAULT_EMAIL);

        // Get all the pessoaList where email equals to UPDATED_EMAIL
        defaultPessoaShouldNotBeFound("email.equals=" + UPDATED_EMAIL);
    }

    @Test
    void getAllPessoasByEmailIsInShouldWork() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where email in DEFAULT_EMAIL or UPDATED_EMAIL
        defaultPessoaShouldBeFound("email.in=" + DEFAULT_EMAIL + "," + UPDATED_EMAIL);

        // Get all the pessoaList where email equals to UPDATED_EMAIL
        defaultPessoaShouldNotBeFound("email.in=" + UPDATED_EMAIL);
    }

    @Test
    void getAllPessoasByEmailIsNullOrNotNull() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where email is not null
        defaultPessoaShouldBeFound("email.specified=true");

        // Get all the pessoaList where email is null
        defaultPessoaShouldNotBeFound("email.specified=false");
    }

    @Test
    void getAllPessoasByEmailContainsSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where email contains DEFAULT_EMAIL
        defaultPessoaShouldBeFound("email.contains=" + DEFAULT_EMAIL);

        // Get all the pessoaList where email contains UPDATED_EMAIL
        defaultPessoaShouldNotBeFound("email.contains=" + UPDATED_EMAIL);
    }

    @Test
    void getAllPessoasByEmailNotContainsSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where email does not contain DEFAULT_EMAIL
        defaultPessoaShouldNotBeFound("email.doesNotContain=" + DEFAULT_EMAIL);

        // Get all the pessoaList where email does not contain UPDATED_EMAIL
        defaultPessoaShouldBeFound("email.doesNotContain=" + UPDATED_EMAIL);
    }

    @Test
    void getAllPessoasBySexoIsEqualToSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where sexo equals to DEFAULT_SEXO
        defaultPessoaShouldBeFound("sexo.equals=" + DEFAULT_SEXO);

        // Get all the pessoaList where sexo equals to UPDATED_SEXO
        defaultPessoaShouldNotBeFound("sexo.equals=" + UPDATED_SEXO);
    }

    @Test
    void getAllPessoasBySexoIsInShouldWork() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where sexo in DEFAULT_SEXO or UPDATED_SEXO
        defaultPessoaShouldBeFound("sexo.in=" + DEFAULT_SEXO + "," + UPDATED_SEXO);

        // Get all the pessoaList where sexo equals to UPDATED_SEXO
        defaultPessoaShouldNotBeFound("sexo.in=" + UPDATED_SEXO);
    }

    @Test
    void getAllPessoasBySexoIsNullOrNotNull() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where sexo is not null
        defaultPessoaShouldBeFound("sexo.specified=true");

        // Get all the pessoaList where sexo is null
        defaultPessoaShouldNotBeFound("sexo.specified=false");
    }

    @Test
    void getAllPessoasByTelefoneIsEqualToSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where telefone equals to DEFAULT_TELEFONE
        defaultPessoaShouldBeFound("telefone.equals=" + DEFAULT_TELEFONE);

        // Get all the pessoaList where telefone equals to UPDATED_TELEFONE
        defaultPessoaShouldNotBeFound("telefone.equals=" + UPDATED_TELEFONE);
    }

    @Test
    void getAllPessoasByTelefoneIsInShouldWork() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where telefone in DEFAULT_TELEFONE or UPDATED_TELEFONE
        defaultPessoaShouldBeFound("telefone.in=" + DEFAULT_TELEFONE + "," + UPDATED_TELEFONE);

        // Get all the pessoaList where telefone equals to UPDATED_TELEFONE
        defaultPessoaShouldNotBeFound("telefone.in=" + UPDATED_TELEFONE);
    }

    @Test
    void getAllPessoasByTelefoneIsNullOrNotNull() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where telefone is not null
        defaultPessoaShouldBeFound("telefone.specified=true");

        // Get all the pessoaList where telefone is null
        defaultPessoaShouldNotBeFound("telefone.specified=false");
    }

    @Test
    void getAllPessoasByTelefoneIsGreaterThanOrEqualToSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where telefone is greater than or equal to DEFAULT_TELEFONE
        defaultPessoaShouldBeFound("telefone.greaterThanOrEqual=" + DEFAULT_TELEFONE);

        // Get all the pessoaList where telefone is greater than or equal to (DEFAULT_TELEFONE + 1)
        defaultPessoaShouldNotBeFound("telefone.greaterThanOrEqual=" + (DEFAULT_TELEFONE + 1));
    }

    @Test
    void getAllPessoasByTelefoneIsLessThanOrEqualToSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where telefone is less than or equal to DEFAULT_TELEFONE
        defaultPessoaShouldBeFound("telefone.lessThanOrEqual=" + DEFAULT_TELEFONE);

        // Get all the pessoaList where telefone is less than or equal to SMALLER_TELEFONE
        defaultPessoaShouldNotBeFound("telefone.lessThanOrEqual=" + SMALLER_TELEFONE);
    }

    @Test
    void getAllPessoasByTelefoneIsLessThanSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where telefone is less than DEFAULT_TELEFONE
        defaultPessoaShouldNotBeFound("telefone.lessThan=" + DEFAULT_TELEFONE);

        // Get all the pessoaList where telefone is less than (DEFAULT_TELEFONE + 1)
        defaultPessoaShouldBeFound("telefone.lessThan=" + (DEFAULT_TELEFONE + 1));
    }

    @Test
    void getAllPessoasByTelefoneIsGreaterThanSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where telefone is greater than DEFAULT_TELEFONE
        defaultPessoaShouldNotBeFound("telefone.greaterThan=" + DEFAULT_TELEFONE);

        // Get all the pessoaList where telefone is greater than SMALLER_TELEFONE
        defaultPessoaShouldBeFound("telefone.greaterThan=" + SMALLER_TELEFONE);
    }

    @Test
    void getAllPessoasBySenhaIsEqualToSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where senha equals to DEFAULT_SENHA
        defaultPessoaShouldBeFound("senha.equals=" + DEFAULT_SENHA);

        // Get all the pessoaList where senha equals to UPDATED_SENHA
        defaultPessoaShouldNotBeFound("senha.equals=" + UPDATED_SENHA);
    }

    @Test
    void getAllPessoasBySenhaIsInShouldWork() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where senha in DEFAULT_SENHA or UPDATED_SENHA
        defaultPessoaShouldBeFound("senha.in=" + DEFAULT_SENHA + "," + UPDATED_SENHA);

        // Get all the pessoaList where senha equals to UPDATED_SENHA
        defaultPessoaShouldNotBeFound("senha.in=" + UPDATED_SENHA);
    }

    @Test
    void getAllPessoasBySenhaIsNullOrNotNull() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where senha is not null
        defaultPessoaShouldBeFound("senha.specified=true");

        // Get all the pessoaList where senha is null
        defaultPessoaShouldNotBeFound("senha.specified=false");
    }

    @Test
    void getAllPessoasBySenhaContainsSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where senha contains DEFAULT_SENHA
        defaultPessoaShouldBeFound("senha.contains=" + DEFAULT_SENHA);

        // Get all the pessoaList where senha contains UPDATED_SENHA
        defaultPessoaShouldNotBeFound("senha.contains=" + UPDATED_SENHA);
    }

    @Test
    void getAllPessoasBySenhaNotContainsSomething() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        // Get all the pessoaList where senha does not contain DEFAULT_SENHA
        defaultPessoaShouldNotBeFound("senha.doesNotContain=" + DEFAULT_SENHA);

        // Get all the pessoaList where senha does not contain UPDATED_SENHA
        defaultPessoaShouldBeFound("senha.doesNotContain=" + UPDATED_SENHA);
    }

    /**
     * Executes the search, and checks that the default entity is returned.
     */
    private void defaultPessoaShouldBeFound(String filter) {
        webTestClient
            .get()
            .uri(ENTITY_API_URL + "?sort=id,desc&" + filter)
            .accept(MediaType.APPLICATION_JSON)
            .exchange()
            .expectStatus()
            .isOk()
            .expectHeader()
            .contentType(MediaType.APPLICATION_JSON)
            .expectBody()
            .jsonPath("$.[*].id")
            .value(hasItem(pessoa.getId().intValue()))
            .jsonPath("$.[*].idPessoa")
            .value(hasItem(DEFAULT_ID_PESSOA))
            .jsonPath("$.[*].nome")
            .value(hasItem(DEFAULT_NOME))
            .jsonPath("$.[*].dataNascimento")
            .value(hasItem(DEFAULT_DATA_NASCIMENTO.toString()))
            .jsonPath("$.[*].email")
            .value(hasItem(DEFAULT_EMAIL))
            .jsonPath("$.[*].sexo")
            .value(hasItem(DEFAULT_SEXO.toString()))
            .jsonPath("$.[*].telefone")
            .value(hasItem(DEFAULT_TELEFONE))
            .jsonPath("$.[*].senha")
            .value(hasItem(DEFAULT_SENHA));

        // Check, that the count call also returns 1
        webTestClient
            .get()
            .uri(ENTITY_API_URL + "/count?sort=id,desc&" + filter)
            .accept(MediaType.APPLICATION_JSON)
            .exchange()
            .expectStatus()
            .isOk()
            .expectHeader()
            .contentType(MediaType.APPLICATION_JSON)
            .expectBody()
            .jsonPath("$")
            .value(is(1));
    }

    /**
     * Executes the search, and checks that the default entity is not returned.
     */
    private void defaultPessoaShouldNotBeFound(String filter) {
        webTestClient
            .get()
            .uri(ENTITY_API_URL + "?sort=id,desc&" + filter)
            .accept(MediaType.APPLICATION_JSON)
            .exchange()
            .expectStatus()
            .isOk()
            .expectHeader()
            .contentType(MediaType.APPLICATION_JSON)
            .expectBody()
            .jsonPath("$")
            .isArray()
            .jsonPath("$")
            .isEmpty();

        // Check, that the count call also returns 0
        webTestClient
            .get()
            .uri(ENTITY_API_URL + "/count?sort=id,desc&" + filter)
            .accept(MediaType.APPLICATION_JSON)
            .exchange()
            .expectStatus()
            .isOk()
            .expectHeader()
            .contentType(MediaType.APPLICATION_JSON)
            .expectBody()
            .jsonPath("$")
            .value(is(0));
    }

    @Test
    void getNonExistingPessoa() {
        // Get the pessoa
        webTestClient
            .get()
            .uri(ENTITY_API_URL_ID, Long.MAX_VALUE)
            .accept(MediaType.APPLICATION_PROBLEM_JSON)
            .exchange()
            .expectStatus()
            .isNotFound();
    }

    @Test
    void putExistingPessoa() throws Exception {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        int databaseSizeBeforeUpdate = pessoaRepository.findAll().collectList().block().size();

        // Update the pessoa
        Pessoa updatedPessoa = pessoaRepository.findById(pessoa.getId()).block();
        updatedPessoa
            .idPessoa(UPDATED_ID_PESSOA)
            .nome(UPDATED_NOME)
            .dataNascimento(UPDATED_DATA_NASCIMENTO)
            .email(UPDATED_EMAIL)
            .sexo(UPDATED_SEXO)
            .telefone(UPDATED_TELEFONE)
            .senha(UPDATED_SENHA);
        PessoaDTO pessoaDTO = pessoaMapper.toDto(updatedPessoa);

        webTestClient
            .put()
            .uri(ENTITY_API_URL_ID, pessoaDTO.getId())
            .contentType(MediaType.APPLICATION_JSON)
            .bodyValue(TestUtil.convertObjectToJsonBytes(pessoaDTO))
            .exchange()
            .expectStatus()
            .isOk();

        // Validate the Pessoa in the database
        List<Pessoa> pessoaList = pessoaRepository.findAll().collectList().block();
        assertThat(pessoaList).hasSize(databaseSizeBeforeUpdate);
        Pessoa testPessoa = pessoaList.get(pessoaList.size() - 1);
        assertThat(testPessoa.getIdPessoa()).isEqualTo(UPDATED_ID_PESSOA);
        assertThat(testPessoa.getNome()).isEqualTo(UPDATED_NOME);
        assertThat(testPessoa.getDataNascimento()).isEqualTo(UPDATED_DATA_NASCIMENTO);
        assertThat(testPessoa.getEmail()).isEqualTo(UPDATED_EMAIL);
        assertThat(testPessoa.getSexo()).isEqualTo(UPDATED_SEXO);
        assertThat(testPessoa.getTelefone()).isEqualTo(UPDATED_TELEFONE);
        assertThat(testPessoa.getSenha()).isEqualTo(UPDATED_SENHA);
    }

    @Test
    void putNonExistingPessoa() throws Exception {
        int databaseSizeBeforeUpdate = pessoaRepository.findAll().collectList().block().size();
        pessoa.setId(count.incrementAndGet());

        // Create the Pessoa
        PessoaDTO pessoaDTO = pessoaMapper.toDto(pessoa);

        // If the entity doesn't have an ID, it will throw BadRequestAlertException
        webTestClient
            .put()
            .uri(ENTITY_API_URL_ID, pessoaDTO.getId())
            .contentType(MediaType.APPLICATION_JSON)
            .bodyValue(TestUtil.convertObjectToJsonBytes(pessoaDTO))
            .exchange()
            .expectStatus()
            .isBadRequest();

        // Validate the Pessoa in the database
        List<Pessoa> pessoaList = pessoaRepository.findAll().collectList().block();
        assertThat(pessoaList).hasSize(databaseSizeBeforeUpdate);
    }

    @Test
    void putWithIdMismatchPessoa() throws Exception {
        int databaseSizeBeforeUpdate = pessoaRepository.findAll().collectList().block().size();
        pessoa.setId(count.incrementAndGet());

        // Create the Pessoa
        PessoaDTO pessoaDTO = pessoaMapper.toDto(pessoa);

        // If url ID doesn't match entity ID, it will throw BadRequestAlertException
        webTestClient
            .put()
            .uri(ENTITY_API_URL_ID, count.incrementAndGet())
            .contentType(MediaType.APPLICATION_JSON)
            .bodyValue(TestUtil.convertObjectToJsonBytes(pessoaDTO))
            .exchange()
            .expectStatus()
            .isBadRequest();

        // Validate the Pessoa in the database
        List<Pessoa> pessoaList = pessoaRepository.findAll().collectList().block();
        assertThat(pessoaList).hasSize(databaseSizeBeforeUpdate);
    }

    @Test
    void putWithMissingIdPathParamPessoa() throws Exception {
        int databaseSizeBeforeUpdate = pessoaRepository.findAll().collectList().block().size();
        pessoa.setId(count.incrementAndGet());

        // Create the Pessoa
        PessoaDTO pessoaDTO = pessoaMapper.toDto(pessoa);

        // If url ID doesn't match entity ID, it will throw BadRequestAlertException
        webTestClient
            .put()
            .uri(ENTITY_API_URL)
            .contentType(MediaType.APPLICATION_JSON)
            .bodyValue(TestUtil.convertObjectToJsonBytes(pessoaDTO))
            .exchange()
            .expectStatus()
            .isEqualTo(405);

        // Validate the Pessoa in the database
        List<Pessoa> pessoaList = pessoaRepository.findAll().collectList().block();
        assertThat(pessoaList).hasSize(databaseSizeBeforeUpdate);
    }

    @Test
    void partialUpdatePessoaWithPatch() throws Exception {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        int databaseSizeBeforeUpdate = pessoaRepository.findAll().collectList().block().size();

        // Update the pessoa using partial update
        Pessoa partialUpdatedPessoa = new Pessoa();
        partialUpdatedPessoa.setId(pessoa.getId());

        partialUpdatedPessoa.idPessoa(UPDATED_ID_PESSOA).dataNascimento(UPDATED_DATA_NASCIMENTO).email(UPDATED_EMAIL);

        webTestClient
            .patch()
            .uri(ENTITY_API_URL_ID, partialUpdatedPessoa.getId())
            .contentType(MediaType.valueOf("application/merge-patch+json"))
            .bodyValue(TestUtil.convertObjectToJsonBytes(partialUpdatedPessoa))
            .exchange()
            .expectStatus()
            .isOk();

        // Validate the Pessoa in the database
        List<Pessoa> pessoaList = pessoaRepository.findAll().collectList().block();
        assertThat(pessoaList).hasSize(databaseSizeBeforeUpdate);
        Pessoa testPessoa = pessoaList.get(pessoaList.size() - 1);
        assertThat(testPessoa.getIdPessoa()).isEqualTo(UPDATED_ID_PESSOA);
        assertThat(testPessoa.getNome()).isEqualTo(DEFAULT_NOME);
        assertThat(testPessoa.getDataNascimento()).isEqualTo(UPDATED_DATA_NASCIMENTO);
        assertThat(testPessoa.getEmail()).isEqualTo(UPDATED_EMAIL);
        assertThat(testPessoa.getSexo()).isEqualTo(DEFAULT_SEXO);
        assertThat(testPessoa.getTelefone()).isEqualTo(DEFAULT_TELEFONE);
        assertThat(testPessoa.getSenha()).isEqualTo(DEFAULT_SENHA);
    }

    @Test
    void fullUpdatePessoaWithPatch() throws Exception {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        int databaseSizeBeforeUpdate = pessoaRepository.findAll().collectList().block().size();

        // Update the pessoa using partial update
        Pessoa partialUpdatedPessoa = new Pessoa();
        partialUpdatedPessoa.setId(pessoa.getId());

        partialUpdatedPessoa
            .idPessoa(UPDATED_ID_PESSOA)
            .nome(UPDATED_NOME)
            .dataNascimento(UPDATED_DATA_NASCIMENTO)
            .email(UPDATED_EMAIL)
            .sexo(UPDATED_SEXO)
            .telefone(UPDATED_TELEFONE)
            .senha(UPDATED_SENHA);

        webTestClient
            .patch()
            .uri(ENTITY_API_URL_ID, partialUpdatedPessoa.getId())
            .contentType(MediaType.valueOf("application/merge-patch+json"))
            .bodyValue(TestUtil.convertObjectToJsonBytes(partialUpdatedPessoa))
            .exchange()
            .expectStatus()
            .isOk();

        // Validate the Pessoa in the database
        List<Pessoa> pessoaList = pessoaRepository.findAll().collectList().block();
        assertThat(pessoaList).hasSize(databaseSizeBeforeUpdate);
        Pessoa testPessoa = pessoaList.get(pessoaList.size() - 1);
        assertThat(testPessoa.getIdPessoa()).isEqualTo(UPDATED_ID_PESSOA);
        assertThat(testPessoa.getNome()).isEqualTo(UPDATED_NOME);
        assertThat(testPessoa.getDataNascimento()).isEqualTo(UPDATED_DATA_NASCIMENTO);
        assertThat(testPessoa.getEmail()).isEqualTo(UPDATED_EMAIL);
        assertThat(testPessoa.getSexo()).isEqualTo(UPDATED_SEXO);
        assertThat(testPessoa.getTelefone()).isEqualTo(UPDATED_TELEFONE);
        assertThat(testPessoa.getSenha()).isEqualTo(UPDATED_SENHA);
    }

    @Test
    void patchNonExistingPessoa() throws Exception {
        int databaseSizeBeforeUpdate = pessoaRepository.findAll().collectList().block().size();
        pessoa.setId(count.incrementAndGet());

        // Create the Pessoa
        PessoaDTO pessoaDTO = pessoaMapper.toDto(pessoa);

        // If the entity doesn't have an ID, it will throw BadRequestAlertException
        webTestClient
            .patch()
            .uri(ENTITY_API_URL_ID, pessoaDTO.getId())
            .contentType(MediaType.valueOf("application/merge-patch+json"))
            .bodyValue(TestUtil.convertObjectToJsonBytes(pessoaDTO))
            .exchange()
            .expectStatus()
            .isBadRequest();

        // Validate the Pessoa in the database
        List<Pessoa> pessoaList = pessoaRepository.findAll().collectList().block();
        assertThat(pessoaList).hasSize(databaseSizeBeforeUpdate);
    }

    @Test
    void patchWithIdMismatchPessoa() throws Exception {
        int databaseSizeBeforeUpdate = pessoaRepository.findAll().collectList().block().size();
        pessoa.setId(count.incrementAndGet());

        // Create the Pessoa
        PessoaDTO pessoaDTO = pessoaMapper.toDto(pessoa);

        // If url ID doesn't match entity ID, it will throw BadRequestAlertException
        webTestClient
            .patch()
            .uri(ENTITY_API_URL_ID, count.incrementAndGet())
            .contentType(MediaType.valueOf("application/merge-patch+json"))
            .bodyValue(TestUtil.convertObjectToJsonBytes(pessoaDTO))
            .exchange()
            .expectStatus()
            .isBadRequest();

        // Validate the Pessoa in the database
        List<Pessoa> pessoaList = pessoaRepository.findAll().collectList().block();
        assertThat(pessoaList).hasSize(databaseSizeBeforeUpdate);
    }

    @Test
    void patchWithMissingIdPathParamPessoa() throws Exception {
        int databaseSizeBeforeUpdate = pessoaRepository.findAll().collectList().block().size();
        pessoa.setId(count.incrementAndGet());

        // Create the Pessoa
        PessoaDTO pessoaDTO = pessoaMapper.toDto(pessoa);

        // If url ID doesn't match entity ID, it will throw BadRequestAlertException
        webTestClient
            .patch()
            .uri(ENTITY_API_URL)
            .contentType(MediaType.valueOf("application/merge-patch+json"))
            .bodyValue(TestUtil.convertObjectToJsonBytes(pessoaDTO))
            .exchange()
            .expectStatus()
            .isEqualTo(405);

        // Validate the Pessoa in the database
        List<Pessoa> pessoaList = pessoaRepository.findAll().collectList().block();
        assertThat(pessoaList).hasSize(databaseSizeBeforeUpdate);
    }

    @Test
    void deletePessoa() {
        // Initialize the database
        pessoaRepository.save(pessoa).block();

        int databaseSizeBeforeDelete = pessoaRepository.findAll().collectList().block().size();

        // Delete the pessoa
        webTestClient
            .delete()
            .uri(ENTITY_API_URL_ID, pessoa.getId())
            .accept(MediaType.APPLICATION_JSON)
            .exchange()
            .expectStatus()
            .isNoContent();

        // Validate the database contains one less item
        List<Pessoa> pessoaList = pessoaRepository.findAll().collectList().block();
        assertThat(pessoaList).hasSize(databaseSizeBeforeDelete - 1);
    }
}
