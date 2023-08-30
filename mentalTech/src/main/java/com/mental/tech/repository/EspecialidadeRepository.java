package com.mental.tech.repository;

import com.mental.tech.domain.Especialidade;
import com.mental.tech.domain.criteria.EspecialidadeCriteria;
import org.springframework.data.domain.Pageable;
import org.springframework.data.r2dbc.repository.Query;
import org.springframework.data.relational.core.query.Criteria;
import org.springframework.data.repository.reactive.ReactiveCrudRepository;
import org.springframework.stereotype.Repository;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

/**
 * Spring Data R2DBC repository for the Especialidade entity.
 */
@SuppressWarnings("unused")
@Repository
public interface EspecialidadeRepository extends ReactiveCrudRepository<Especialidade, Long>, EspecialidadeRepositoryInternal {
    Flux<Especialidade> findAllBy(Pageable pageable);

    @Override
    <S extends Especialidade> Mono<S> save(S entity);

    @Override
    Flux<Especialidade> findAll();

    @Override
    Mono<Especialidade> findById(Long id);

    @Override
    Mono<Void> deleteById(Long id);
}

interface EspecialidadeRepositoryInternal {
    <S extends Especialidade> Mono<S> save(S entity);

    Flux<Especialidade> findAllBy(Pageable pageable);

    Flux<Especialidade> findAll();

    Mono<Especialidade> findById(Long id);
    // this is not supported at the moment because of https://github.com/jhipster/generator-jhipster/issues/18269
    // Flux<Especialidade> findAllBy(Pageable pageable, Criteria criteria);
    Flux<Especialidade> findByCriteria(EspecialidadeCriteria criteria, Pageable pageable);

    Mono<Long> countByCriteria(EspecialidadeCriteria criteria);
}
