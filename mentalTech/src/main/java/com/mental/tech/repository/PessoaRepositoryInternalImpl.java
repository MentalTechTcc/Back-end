package com.mental.tech.repository;


import com.mental.tech.domain.Pessoa;
import com.mental.tech.domain.criteria.PessoaCriteria;
import com.mental.tech.repository.rowmapper.ColumnConverter;
import com.mental.tech.repository.rowmapper.PessoaRowMapper;
import io.r2dbc.spi.Row;
import io.r2dbc.spi.RowMetadata;
import java.util.ArrayList;
import java.util.List;
import org.springframework.data.domain.Pageable;
import org.springframework.data.r2dbc.convert.R2dbcConverter;
import org.springframework.data.r2dbc.core.R2dbcEntityOperations;
import org.springframework.data.r2dbc.core.R2dbcEntityTemplate;
import org.springframework.data.r2dbc.repository.support.SimpleR2dbcRepository;
import org.springframework.data.relational.core.sql.Comparison;
import org.springframework.data.relational.core.sql.Condition;
import org.springframework.data.relational.core.sql.Conditions;
import org.springframework.data.relational.core.sql.Expression;
import org.springframework.data.relational.core.sql.Select;
import org.springframework.data.relational.core.sql.SelectBuilder.SelectFromAndJoin;
import org.springframework.data.relational.core.sql.Table;
import org.springframework.data.relational.repository.support.MappingRelationalEntityInformation;
import org.springframework.r2dbc.core.DatabaseClient;
import org.springframework.r2dbc.core.RowsFetchSpec;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;
import tech.jhipster.service.ConditionBuilder;

/**
 * Spring Data R2DBC custom repository implementation for the Pessoa entity.
 */
@SuppressWarnings("unused")
class PessoaRepositoryInternalImpl extends SimpleR2dbcRepository<Pessoa, Long> implements PessoaRepositoryInternal {

    private final DatabaseClient db;
    private final R2dbcEntityTemplate r2dbcEntityTemplate;
    private final EntityManager entityManager;

    private final PessoaRowMapper pessoaMapper;
    private final ColumnConverter columnConverter;

    private static final Table entityTable = Table.aliased("pessoa", EntityManager.ENTITY_ALIAS);

    public PessoaRepositoryInternalImpl(
        R2dbcEntityTemplate template,
        EntityManager entityManager,
        PessoaRowMapper pessoaMapper,
        R2dbcEntityOperations entityOperations,
        R2dbcConverter converter,
        ColumnConverter columnConverter
    ) {
        super(
            new MappingRelationalEntityInformation(converter.getMappingContext().getRequiredPersistentEntity(Pessoa.class)),
            entityOperations,
            converter
        );
        this.db = template.getDatabaseClient();
        this.r2dbcEntityTemplate = template;
        this.entityManager = entityManager;
        this.pessoaMapper = pessoaMapper;
        this.columnConverter = columnConverter;
    }

    @Override
    public Flux<Pessoa> findAllBy(Pageable pageable) {
        return createQuery(pageable, null).all();
    }

    RowsFetchSpec<Pessoa> createQuery(Pageable pageable, Condition whereClause) {
        List<Expression> columns = PessoaSqlHelper.getColumns(entityTable, EntityManager.ENTITY_ALIAS);
        SelectFromAndJoin selectFrom = Select.builder().select(columns).from(entityTable);
        // we do not support Criteria here for now as of https://github.com/jhipster/generator-jhipster/issues/18269
        String select = entityManager.createSelect(selectFrom, Pessoa.class, pageable, whereClause);
        return db.sql(select).map(this::process);
    }

    @Override
    public Flux<Pessoa> findAll() {
        return findAllBy(null);
    }

    @Override
    public Mono<Pessoa> findById(Long id) {
        Comparison whereClause = Conditions.isEqual(entityTable.column("id"), Conditions.just(id.toString()));
        return createQuery(null, whereClause).one();
    }

    private Pessoa process(Row row, RowMetadata metadata) {
        Pessoa entity = pessoaMapper.apply(row, "e");
        return entity;
    }

    @Override
    public <S extends Pessoa> Mono<S> save(S entity) {
        return super.save(entity);
    }

    @Override
    public Flux<Pessoa> findByCriteria(PessoaCriteria pessoaCriteria, Pageable page) {
        return createQuery(page, buildConditions(pessoaCriteria)).all();
    }

    @Override
    public Mono<Long> countByCriteria(PessoaCriteria criteria) {
        return findByCriteria(criteria, null)
            .collectList()
            .map(collectedList -> collectedList != null ? (long) collectedList.size() : (long) 0);
    }

    private Condition buildConditions(PessoaCriteria criteria) {
        ConditionBuilder builder = new ConditionBuilder(this.columnConverter);
        List<Condition> allConditions = new ArrayList<Condition>();
        if (criteria != null) {
            if (criteria.getId() != null) {
                builder.buildFilterConditionForField(criteria.getId(), entityTable.column("id"));
            }
            if (criteria.getIdPessoa() != null) {
                builder.buildFilterConditionForField(criteria.getIdPessoa(), entityTable.column("id_pessoa"));
            }
            if (criteria.getNome() != null) {
                builder.buildFilterConditionForField(criteria.getNome(), entityTable.column("nome"));
            }
            if (criteria.getDataNascimento() != null) {
                builder.buildFilterConditionForField(criteria.getDataNascimento(), entityTable.column("data_nascimento"));
            }
            if (criteria.getEmail() != null) {
                builder.buildFilterConditionForField(criteria.getEmail(), entityTable.column("email"));
            }
            if (criteria.getSexo() != null) {
                builder.buildFilterConditionForField(criteria.getSexo(), entityTable.column("sexo"));
            }
            if (criteria.getTelefone() != null) {
                builder.buildFilterConditionForField(criteria.getTelefone(), entityTable.column("telefone"));
            }
            if (criteria.getSenha() != null) {
                builder.buildFilterConditionForField(criteria.getSenha(), entityTable.column("senha"));
            }
        }
        return builder.buildConditions();
    }
}
