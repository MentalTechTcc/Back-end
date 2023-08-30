package com.mental.tech.web.rest;

import static org.assertj.core.api.Assertions.assertThat;
import static org.hamcrest.Matchers.hasItem;
import static org.hamcrest.Matchers.is;

import com.mental.tech.IntegrationTest;
import com.mental.tech.domain.Especialidade;
import com.mental.tech.repository.EntityManager;
import com.mental.tech.repository.EspecialidadeRepository;
import java.time.Duration;
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
 * Integration tests for the {@link EspecialidadeResource} REST controller.
 */
@IntegrationTest
@AutoConfigureWebTestClient(timeout = IntegrationTest.DEFAULT_ENTITY_TIMEOUT)
@WithMockUser
class EspecialidadeResourceIT {

    private static final Integer DEFAULT_ID_ESPECIALIDADE = 1;
    private static final Integer UPDATED_ID_ESPECIALIDADE = 2;
    private static final Integer SMALLER_ID_ESPECIALIDADE = 1 - 1;

    private static final String DEFAULT_NOME_ESPECIALIDADE = "AAAAAAAAAA";
    private static final String UPDATED_NOME_ESPECIALIDADE = "BBBBBBBBBB";

    private static final String ENTITY_API_URL = "/api/especialidades";
    private static final String ENTITY_API_URL_ID = ENTITY_API_URL + "/{id}";

    private static Random random = new Random();
    private static AtomicLong count = new AtomicLong(random.nextInt() + (2 * Integer.MAX_VALUE));

    @Autowired
    private EspecialidadeRepository especialidadeRepository;

    @Autowired
    private EntityManager em;

    @Autowired
    private WebTestClient webTestClient;

    private Especialidade especialidade;

    /**
     * Create an entity for this test.
     *
     * This is a static method, as tests for other entities might also need it,
     * if they test an entity which requires the current entity.
     */
    public static Especialidade createEntity(EntityManager em) {
        Especialidade especialidade = new Especialidade()
            .idEspecialidade(DEFAULT_ID_ESPECIALIDADE)
            .nomeEspecialidade(DEFAULT_NOME_ESPECIALIDADE);
        return especialidade;
    }

    /**
     * Create an updated entity for this test.
     *
     * This is a static method, as tests for other entities might also need it,
     * if they test an entity which requires the current entity.
     */
    public static Especialidade createUpdatedEntity(EntityManager em) {
        Especialidade especialidade = new Especialidade()
            .idEspecialidade(UPDATED_ID_ESPECIALIDADE)
            .nomeEspecialidade(UPDATED_NOME_ESPECIALIDADE);
        return especialidade;
    }

    public static void deleteEntities(EntityManager em) {
        try {
            em.deleteAll(Especialidade.class).block();
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
        especialidade = createEntity(em);
    }

    @Test
    void createEspecialidade() throws Exception {
        int databaseSizeBeforeCreate = especialidadeRepository.findAll().collectList().block().size();
        // Create the Especialidade
        webTestClient
            .post()
            .uri(ENTITY_API_URL)
            .contentType(MediaType.APPLICATION_JSON)
            .bodyValue(TestUtil.convertObjectToJsonBytes(especialidade))
            .exchange()
            .expectStatus()
            .isCreated();

        // Validate the Especialidade in the database
        List<Especialidade> especialidadeList = especialidadeRepository.findAll().collectList().block();
        assertThat(especialidadeList).hasSize(databaseSizeBeforeCreate + 1);
        Especialidade testEspecialidade = especialidadeList.get(especialidadeList.size() - 1);
        assertThat(testEspecialidade.getIdEspecialidade()).isEqualTo(DEFAULT_ID_ESPECIALIDADE);
        assertThat(testEspecialidade.getNomeEspecialidade()).isEqualTo(DEFAULT_NOME_ESPECIALIDADE);
    }

    @Test
    void createEspecialidadeWithExistingId() throws Exception {
        // Create the Especialidade with an existing ID
        especialidade.setId(1L);

        int databaseSizeBeforeCreate = especialidadeRepository.findAll().collectList().block().size();

        // An entity with an existing ID cannot be created, so this API call must fail
        webTestClient
            .post()
            .uri(ENTITY_API_URL)
            .contentType(MediaType.APPLICATION_JSON)
            .bodyValue(TestUtil.convertObjectToJsonBytes(especialidade))
            .exchange()
            .expectStatus()
            .isBadRequest();

        // Validate the Especialidade in the database
        List<Especialidade> especialidadeList = especialidadeRepository.findAll().collectList().block();
        assertThat(especialidadeList).hasSize(databaseSizeBeforeCreate);
    }

    @Test
    void checkIdEspecialidadeIsRequired() throws Exception {
        int databaseSizeBeforeTest = especialidadeRepository.findAll().collectList().block().size();
        // set the field null
        especialidade.setIdEspecialidade(null);

        // Create the Especialidade, which fails.

        webTestClient
            .post()
            .uri(ENTITY_API_URL)
            .contentType(MediaType.APPLICATION_JSON)
            .bodyValue(TestUtil.convertObjectToJsonBytes(especialidade))
            .exchange()
            .expectStatus()
            .isBadRequest();

        List<Especialidade> especialidadeList = especialidadeRepository.findAll().collectList().block();
        assertThat(especialidadeList).hasSize(databaseSizeBeforeTest);
    }

    @Test
    void getAllEspecialidades() {
        // Initialize the database
        especialidadeRepository.save(especialidade).block();

        // Get all the especialidadeList
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
            .value(hasItem(especialidade.getId().intValue()))
            .jsonPath("$.[*].idEspecialidade")
            .value(hasItem(DEFAULT_ID_ESPECIALIDADE))
            .jsonPath("$.[*].nomeEspecialidade")
            .value(hasItem(DEFAULT_NOME_ESPECIALIDADE));
    }

    @Test
    void getEspecialidade() {
        // Initialize the database
        especialidadeRepository.save(especialidade).block();

        // Get the especialidade
        webTestClient
            .get()
            .uri(ENTITY_API_URL_ID, especialidade.getId())
            .accept(MediaType.APPLICATION_JSON)
            .exchange()
            .expectStatus()
            .isOk()
            .expectHeader()
            .contentType(MediaType.APPLICATION_JSON)
            .expectBody()
            .jsonPath("$.id")
            .value(is(especialidade.getId().intValue()))
            .jsonPath("$.idEspecialidade")
            .value(is(DEFAULT_ID_ESPECIALIDADE))
            .jsonPath("$.nomeEspecialidade")
            .value(is(DEFAULT_NOME_ESPECIALIDADE));
    }

    @Test
    void getEspecialidadesByIdFiltering() {
        // Initialize the database
        especialidadeRepository.save(especialidade).block();

        Long id = especialidade.getId();

        defaultEspecialidadeShouldBeFound("id.equals=" + id);
        defaultEspecialidadeShouldNotBeFound("id.notEquals=" + id);

        defaultEspecialidadeShouldBeFound("id.greaterThanOrEqual=" + id);
        defaultEspecialidadeShouldNotBeFound("id.greaterThan=" + id);

        defaultEspecialidadeShouldBeFound("id.lessThanOrEqual=" + id);
        defaultEspecialidadeShouldNotBeFound("id.lessThan=" + id);
    }

    @Test
    void getAllEspecialidadesByIdEspecialidadeIsEqualToSomething() {
        // Initialize the database
        especialidadeRepository.save(especialidade).block();

        // Get all the especialidadeList where idEspecialidade equals to DEFAULT_ID_ESPECIALIDADE
        defaultEspecialidadeShouldBeFound("idEspecialidade.equals=" + DEFAULT_ID_ESPECIALIDADE);

        // Get all the especialidadeList where idEspecialidade equals to UPDATED_ID_ESPECIALIDADE
        defaultEspecialidadeShouldNotBeFound("idEspecialidade.equals=" + UPDATED_ID_ESPECIALIDADE);
    }

    @Test
    void getAllEspecialidadesByIdEspecialidadeIsInShouldWork() {
        // Initialize the database
        especialidadeRepository.save(especialidade).block();

        // Get all the especialidadeList where idEspecialidade in DEFAULT_ID_ESPECIALIDADE or UPDATED_ID_ESPECIALIDADE
        defaultEspecialidadeShouldBeFound("idEspecialidade.in=" + DEFAULT_ID_ESPECIALIDADE + "," + UPDATED_ID_ESPECIALIDADE);

        // Get all the especialidadeList where idEspecialidade equals to UPDATED_ID_ESPECIALIDADE
        defaultEspecialidadeShouldNotBeFound("idEspecialidade.in=" + UPDATED_ID_ESPECIALIDADE);
    }

    @Test
    void getAllEspecialidadesByIdEspecialidadeIsNullOrNotNull() {
        // Initialize the database
        especialidadeRepository.save(especialidade).block();

        // Get all the especialidadeList where idEspecialidade is not null
        defaultEspecialidadeShouldBeFound("idEspecialidade.specified=true");

        // Get all the especialidadeList where idEspecialidade is null
        defaultEspecialidadeShouldNotBeFound("idEspecialidade.specified=false");
    }

    @Test
    void getAllEspecialidadesByIdEspecialidadeIsGreaterThanOrEqualToSomething() {
        // Initialize the database
        especialidadeRepository.save(especialidade).block();

        // Get all the especialidadeList where idEspecialidade is greater than or equal to DEFAULT_ID_ESPECIALIDADE
        defaultEspecialidadeShouldBeFound("idEspecialidade.greaterThanOrEqual=" + DEFAULT_ID_ESPECIALIDADE);

        // Get all the especialidadeList where idEspecialidade is greater than or equal to UPDATED_ID_ESPECIALIDADE
        defaultEspecialidadeShouldNotBeFound("idEspecialidade.greaterThanOrEqual=" + UPDATED_ID_ESPECIALIDADE);
    }

    @Test
    void getAllEspecialidadesByIdEspecialidadeIsLessThanOrEqualToSomething() {
        // Initialize the database
        especialidadeRepository.save(especialidade).block();

        // Get all the especialidadeList where idEspecialidade is less than or equal to DEFAULT_ID_ESPECIALIDADE
        defaultEspecialidadeShouldBeFound("idEspecialidade.lessThanOrEqual=" + DEFAULT_ID_ESPECIALIDADE);

        // Get all the especialidadeList where idEspecialidade is less than or equal to SMALLER_ID_ESPECIALIDADE
        defaultEspecialidadeShouldNotBeFound("idEspecialidade.lessThanOrEqual=" + SMALLER_ID_ESPECIALIDADE);
    }

    @Test
    void getAllEspecialidadesByIdEspecialidadeIsLessThanSomething() {
        // Initialize the database
        especialidadeRepository.save(especialidade).block();

        // Get all the especialidadeList where idEspecialidade is less than DEFAULT_ID_ESPECIALIDADE
        defaultEspecialidadeShouldNotBeFound("idEspecialidade.lessThan=" + DEFAULT_ID_ESPECIALIDADE);

        // Get all the especialidadeList where idEspecialidade is less than UPDATED_ID_ESPECIALIDADE
        defaultEspecialidadeShouldBeFound("idEspecialidade.lessThan=" + UPDATED_ID_ESPECIALIDADE);
    }

    @Test
    void getAllEspecialidadesByIdEspecialidadeIsGreaterThanSomething() {
        // Initialize the database
        especialidadeRepository.save(especialidade).block();

        // Get all the especialidadeList where idEspecialidade is greater than DEFAULT_ID_ESPECIALIDADE
        defaultEspecialidadeShouldNotBeFound("idEspecialidade.greaterThan=" + DEFAULT_ID_ESPECIALIDADE);

        // Get all the especialidadeList where idEspecialidade is greater than SMALLER_ID_ESPECIALIDADE
        defaultEspecialidadeShouldBeFound("idEspecialidade.greaterThan=" + SMALLER_ID_ESPECIALIDADE);
    }

    @Test
    void getAllEspecialidadesByNomeEspecialidadeIsEqualToSomething() {
        // Initialize the database
        especialidadeRepository.save(especialidade).block();

        // Get all the especialidadeList where nomeEspecialidade equals to DEFAULT_NOME_ESPECIALIDADE
        defaultEspecialidadeShouldBeFound("nomeEspecialidade.equals=" + DEFAULT_NOME_ESPECIALIDADE);

        // Get all the especialidadeList where nomeEspecialidade equals to UPDATED_NOME_ESPECIALIDADE
        defaultEspecialidadeShouldNotBeFound("nomeEspecialidade.equals=" + UPDATED_NOME_ESPECIALIDADE);
    }

    @Test
    void getAllEspecialidadesByNomeEspecialidadeIsInShouldWork() {
        // Initialize the database
        especialidadeRepository.save(especialidade).block();

        // Get all the especialidadeList where nomeEspecialidade in DEFAULT_NOME_ESPECIALIDADE or UPDATED_NOME_ESPECIALIDADE
        defaultEspecialidadeShouldBeFound("nomeEspecialidade.in=" + DEFAULT_NOME_ESPECIALIDADE + "," + UPDATED_NOME_ESPECIALIDADE);

        // Get all the especialidadeList where nomeEspecialidade equals to UPDATED_NOME_ESPECIALIDADE
        defaultEspecialidadeShouldNotBeFound("nomeEspecialidade.in=" + UPDATED_NOME_ESPECIALIDADE);
    }

    @Test
    void getAllEspecialidadesByNomeEspecialidadeIsNullOrNotNull() {
        // Initialize the database
        especialidadeRepository.save(especialidade).block();

        // Get all the especialidadeList where nomeEspecialidade is not null
        defaultEspecialidadeShouldBeFound("nomeEspecialidade.specified=true");

        // Get all the especialidadeList where nomeEspecialidade is null
        defaultEspecialidadeShouldNotBeFound("nomeEspecialidade.specified=false");
    }

    @Test
    void getAllEspecialidadesByNomeEspecialidadeContainsSomething() {
        // Initialize the database
        especialidadeRepository.save(especialidade).block();

        // Get all the especialidadeList where nomeEspecialidade contains DEFAULT_NOME_ESPECIALIDADE
        defaultEspecialidadeShouldBeFound("nomeEspecialidade.contains=" + DEFAULT_NOME_ESPECIALIDADE);

        // Get all the especialidadeList where nomeEspecialidade contains UPDATED_NOME_ESPECIALIDADE
        defaultEspecialidadeShouldNotBeFound("nomeEspecialidade.contains=" + UPDATED_NOME_ESPECIALIDADE);
    }

    @Test
    void getAllEspecialidadesByNomeEspecialidadeNotContainsSomething() {
        // Initialize the database
        especialidadeRepository.save(especialidade).block();

        // Get all the especialidadeList where nomeEspecialidade does not contain DEFAULT_NOME_ESPECIALIDADE
        defaultEspecialidadeShouldNotBeFound("nomeEspecialidade.doesNotContain=" + DEFAULT_NOME_ESPECIALIDADE);

        // Get all the especialidadeList where nomeEspecialidade does not contain UPDATED_NOME_ESPECIALIDADE
        defaultEspecialidadeShouldBeFound("nomeEspecialidade.doesNotContain=" + UPDATED_NOME_ESPECIALIDADE);
    }

    /**
     * Executes the search, and checks that the default entity is returned.
     */
    private void defaultEspecialidadeShouldBeFound(String filter) {
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
            .value(hasItem(especialidade.getId().intValue()))
            .jsonPath("$.[*].idEspecialidade")
            .value(hasItem(DEFAULT_ID_ESPECIALIDADE))
            .jsonPath("$.[*].nomeEspecialidade")
            .value(hasItem(DEFAULT_NOME_ESPECIALIDADE));

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
    private void defaultEspecialidadeShouldNotBeFound(String filter) {
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
    void getNonExistingEspecialidade() {
        // Get the especialidade
        webTestClient
            .get()
            .uri(ENTITY_API_URL_ID, Long.MAX_VALUE)
            .accept(MediaType.APPLICATION_PROBLEM_JSON)
            .exchange()
            .expectStatus()
            .isNotFound();
    }

    @Test
    void putExistingEspecialidade() throws Exception {
        // Initialize the database
        especialidadeRepository.save(especialidade).block();

        int databaseSizeBeforeUpdate = especialidadeRepository.findAll().collectList().block().size();

        // Update the especialidade
        Especialidade updatedEspecialidade = especialidadeRepository.findById(especialidade.getId()).block();
        updatedEspecialidade.idEspecialidade(UPDATED_ID_ESPECIALIDADE).nomeEspecialidade(UPDATED_NOME_ESPECIALIDADE);

        webTestClient
            .put()
            .uri(ENTITY_API_URL_ID, updatedEspecialidade.getId())
            .contentType(MediaType.APPLICATION_JSON)
            .bodyValue(TestUtil.convertObjectToJsonBytes(updatedEspecialidade))
            .exchange()
            .expectStatus()
            .isOk();

        // Validate the Especialidade in the database
        List<Especialidade> especialidadeList = especialidadeRepository.findAll().collectList().block();
        assertThat(especialidadeList).hasSize(databaseSizeBeforeUpdate);
        Especialidade testEspecialidade = especialidadeList.get(especialidadeList.size() - 1);
        assertThat(testEspecialidade.getIdEspecialidade()).isEqualTo(UPDATED_ID_ESPECIALIDADE);
        assertThat(testEspecialidade.getNomeEspecialidade()).isEqualTo(UPDATED_NOME_ESPECIALIDADE);
    }

    @Test
    void putNonExistingEspecialidade() throws Exception {
        int databaseSizeBeforeUpdate = especialidadeRepository.findAll().collectList().block().size();
        especialidade.setId(count.incrementAndGet());

        // If the entity doesn't have an ID, it will throw BadRequestAlertException
        webTestClient
            .put()
            .uri(ENTITY_API_URL_ID, especialidade.getId())
            .contentType(MediaType.APPLICATION_JSON)
            .bodyValue(TestUtil.convertObjectToJsonBytes(especialidade))
            .exchange()
            .expectStatus()
            .isBadRequest();

        // Validate the Especialidade in the database
        List<Especialidade> especialidadeList = especialidadeRepository.findAll().collectList().block();
        assertThat(especialidadeList).hasSize(databaseSizeBeforeUpdate);
    }

    @Test
    void putWithIdMismatchEspecialidade() throws Exception {
        int databaseSizeBeforeUpdate = especialidadeRepository.findAll().collectList().block().size();
        especialidade.setId(count.incrementAndGet());

        // If url ID doesn't match entity ID, it will throw BadRequestAlertException
        webTestClient
            .put()
            .uri(ENTITY_API_URL_ID, count.incrementAndGet())
            .contentType(MediaType.APPLICATION_JSON)
            .bodyValue(TestUtil.convertObjectToJsonBytes(especialidade))
            .exchange()
            .expectStatus()
            .isBadRequest();

        // Validate the Especialidade in the database
        List<Especialidade> especialidadeList = especialidadeRepository.findAll().collectList().block();
        assertThat(especialidadeList).hasSize(databaseSizeBeforeUpdate);
    }

    @Test
    void putWithMissingIdPathParamEspecialidade() throws Exception {
        int databaseSizeBeforeUpdate = especialidadeRepository.findAll().collectList().block().size();
        especialidade.setId(count.incrementAndGet());

        // If url ID doesn't match entity ID, it will throw BadRequestAlertException
        webTestClient
            .put()
            .uri(ENTITY_API_URL)
            .contentType(MediaType.APPLICATION_JSON)
            .bodyValue(TestUtil.convertObjectToJsonBytes(especialidade))
            .exchange()
            .expectStatus()
            .isEqualTo(405);

        // Validate the Especialidade in the database
        List<Especialidade> especialidadeList = especialidadeRepository.findAll().collectList().block();
        assertThat(especialidadeList).hasSize(databaseSizeBeforeUpdate);
    }

    @Test
    void partialUpdateEspecialidadeWithPatch() throws Exception {
        // Initialize the database
        especialidadeRepository.save(especialidade).block();

        int databaseSizeBeforeUpdate = especialidadeRepository.findAll().collectList().block().size();

        // Update the especialidade using partial update
        Especialidade partialUpdatedEspecialidade = new Especialidade();
        partialUpdatedEspecialidade.setId(especialidade.getId());

        webTestClient
            .patch()
            .uri(ENTITY_API_URL_ID, partialUpdatedEspecialidade.getId())
            .contentType(MediaType.valueOf("application/merge-patch+json"))
            .bodyValue(TestUtil.convertObjectToJsonBytes(partialUpdatedEspecialidade))
            .exchange()
            .expectStatus()
            .isOk();

        // Validate the Especialidade in the database
        List<Especialidade> especialidadeList = especialidadeRepository.findAll().collectList().block();
        assertThat(especialidadeList).hasSize(databaseSizeBeforeUpdate);
        Especialidade testEspecialidade = especialidadeList.get(especialidadeList.size() - 1);
        assertThat(testEspecialidade.getIdEspecialidade()).isEqualTo(DEFAULT_ID_ESPECIALIDADE);
        assertThat(testEspecialidade.getNomeEspecialidade()).isEqualTo(DEFAULT_NOME_ESPECIALIDADE);
    }

    @Test
    void fullUpdateEspecialidadeWithPatch() throws Exception {
        // Initialize the database
        especialidadeRepository.save(especialidade).block();

        int databaseSizeBeforeUpdate = especialidadeRepository.findAll().collectList().block().size();

        // Update the especialidade using partial update
        Especialidade partialUpdatedEspecialidade = new Especialidade();
        partialUpdatedEspecialidade.setId(especialidade.getId());

        partialUpdatedEspecialidade.idEspecialidade(UPDATED_ID_ESPECIALIDADE).nomeEspecialidade(UPDATED_NOME_ESPECIALIDADE);

        webTestClient
            .patch()
            .uri(ENTITY_API_URL_ID, partialUpdatedEspecialidade.getId())
            .contentType(MediaType.valueOf("application/merge-patch+json"))
            .bodyValue(TestUtil.convertObjectToJsonBytes(partialUpdatedEspecialidade))
            .exchange()
            .expectStatus()
            .isOk();

        // Validate the Especialidade in the database
        List<Especialidade> especialidadeList = especialidadeRepository.findAll().collectList().block();
        assertThat(especialidadeList).hasSize(databaseSizeBeforeUpdate);
        Especialidade testEspecialidade = especialidadeList.get(especialidadeList.size() - 1);
        assertThat(testEspecialidade.getIdEspecialidade()).isEqualTo(UPDATED_ID_ESPECIALIDADE);
        assertThat(testEspecialidade.getNomeEspecialidade()).isEqualTo(UPDATED_NOME_ESPECIALIDADE);
    }

    @Test
    void patchNonExistingEspecialidade() throws Exception {
        int databaseSizeBeforeUpdate = especialidadeRepository.findAll().collectList().block().size();
        especialidade.setId(count.incrementAndGet());

        // If the entity doesn't have an ID, it will throw BadRequestAlertException
        webTestClient
            .patch()
            .uri(ENTITY_API_URL_ID, especialidade.getId())
            .contentType(MediaType.valueOf("application/merge-patch+json"))
            .bodyValue(TestUtil.convertObjectToJsonBytes(especialidade))
            .exchange()
            .expectStatus()
            .isBadRequest();

        // Validate the Especialidade in the database
        List<Especialidade> especialidadeList = especialidadeRepository.findAll().collectList().block();
        assertThat(especialidadeList).hasSize(databaseSizeBeforeUpdate);
    }

    @Test
    void patchWithIdMismatchEspecialidade() throws Exception {
        int databaseSizeBeforeUpdate = especialidadeRepository.findAll().collectList().block().size();
        especialidade.setId(count.incrementAndGet());

        // If url ID doesn't match entity ID, it will throw BadRequestAlertException
        webTestClient
            .patch()
            .uri(ENTITY_API_URL_ID, count.incrementAndGet())
            .contentType(MediaType.valueOf("application/merge-patch+json"))
            .bodyValue(TestUtil.convertObjectToJsonBytes(especialidade))
            .exchange()
            .expectStatus()
            .isBadRequest();

        // Validate the Especialidade in the database
        List<Especialidade> especialidadeList = especialidadeRepository.findAll().collectList().block();
        assertThat(especialidadeList).hasSize(databaseSizeBeforeUpdate);
    }

    @Test
    void patchWithMissingIdPathParamEspecialidade() throws Exception {
        int databaseSizeBeforeUpdate = especialidadeRepository.findAll().collectList().block().size();
        especialidade.setId(count.incrementAndGet());

        // If url ID doesn't match entity ID, it will throw BadRequestAlertException
        webTestClient
            .patch()
            .uri(ENTITY_API_URL)
            .contentType(MediaType.valueOf("application/merge-patch+json"))
            .bodyValue(TestUtil.convertObjectToJsonBytes(especialidade))
            .exchange()
            .expectStatus()
            .isEqualTo(405);

        // Validate the Especialidade in the database
        List<Especialidade> especialidadeList = especialidadeRepository.findAll().collectList().block();
        assertThat(especialidadeList).hasSize(databaseSizeBeforeUpdate);
    }

    @Test
    void deleteEspecialidade() {
        // Initialize the database
        especialidadeRepository.save(especialidade).block();

        int databaseSizeBeforeDelete = especialidadeRepository.findAll().collectList().block().size();

        // Delete the especialidade
        webTestClient
            .delete()
            .uri(ENTITY_API_URL_ID, especialidade.getId())
            .accept(MediaType.APPLICATION_JSON)
            .exchange()
            .expectStatus()
            .isNoContent();

        // Validate the database contains one less item
        List<Especialidade> especialidadeList = especialidadeRepository.findAll().collectList().block();
        assertThat(especialidadeList).hasSize(databaseSizeBeforeDelete - 1);
    }
}
