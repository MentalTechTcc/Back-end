package com.mental.tech.repository;

import com.mental.tech.domain.Pessoa;
import com.mental.tech.domain.criteria.PessoaCriteria;
import org.springframework.data.domain.Pageable;
import org.springframework.data.repository.reactive.ReactiveCrudRepository;
import org.springframework.stereotype.Repository;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

/**
 * Spring Data R2DBC repository for the Pessoa entity.
 */
@SuppressWarnings("unused")
@Repository
public interface PessoaRepository extends ReactiveCrudRepository<Pessoa, Long>, PessoaRepositoryInternal {
    Flux<Pessoa> findAllBy(Pageable pageable);

    @Override
    <S extends Pessoa> Mono<S> save(S entity);

    @Override
    Flux<Pessoa> findAll();

    @Override
    Mono<Pessoa> findById(Long id);

    @Override
    Mono<Void> deleteById(Long id);
}

interface PessoaRepositoryInternal {
    <S extends Pessoa> Mono<S> save(S entity);

    Flux<Pessoa> findAllBy(Pageable pageable);

    Flux<Pessoa> findAll();

    Mono<Pessoa> findById(Long id);
    // this is not supported at the moment because of https://github.com/jhipster/generator-jhipster/issues/18269
    // Flux<Pessoa> findAllBy(Pageable pageable, Criteria criteria);
    Flux<Pessoa> findByCriteria(PessoaCriteria criteria, Pageable pageable);

    Mono<Long> countByCriteria(PessoaCriteria criteria);
}
