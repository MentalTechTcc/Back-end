package com.mental.tech.service;

import com.mental.tech.domain.Pessoa;
import com.mental.tech.domain.criteria.PessoaCriteria;
import com.mental.tech.repository.PessoaRepository;
import com.mental.tech.service.dto.PessoaDTO;
import com.mental.tech.service.mapper.PessoaMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

/**
 * Service Implementation for managing {@link Pessoa}.
 */
@Service
@Transactional
public class PessoaService {

    private final Logger log = LoggerFactory.getLogger(PessoaService.class);

    private final PessoaRepository pessoaRepository;

    private final PessoaMapper pessoaMapper;

    public PessoaService(PessoaRepository pessoaRepository, PessoaMapper pessoaMapper) {
        this.pessoaRepository = pessoaRepository;
        this.pessoaMapper = pessoaMapper;
    }

    /**
     * Save a pessoa.
     *
     * @param pessoaDTO the entity to save.
     * @return the persisted entity.
     */
    public Mono<PessoaDTO> save(PessoaDTO pessoaDTO) {
        log.debug("Request to save Pessoa : {}", pessoaDTO);
        return pessoaRepository.save(pessoaMapper.toEntity(pessoaDTO)).map(pessoaMapper::toDto);
    }

    /**
     * Update a pessoa.
     *
     * @param pessoaDTO the entity to save.
     * @return the persisted entity.
     */
    public Mono<PessoaDTO> update(PessoaDTO pessoaDTO) {
        log.debug("Request to update Pessoa : {}", pessoaDTO);
        return pessoaRepository.save(pessoaMapper.toEntity(pessoaDTO)).map(pessoaMapper::toDto);
    }

    /**
     * Partially update a pessoa.
     *
     * @param pessoaDTO the entity to update partially.
     * @return the persisted entity.
     */
    public Mono<PessoaDTO> partialUpdate(PessoaDTO pessoaDTO) {
        log.debug("Request to partially update Pessoa : {}", pessoaDTO);

        return pessoaRepository
            .findById(pessoaDTO.getId())
            .map(existingPessoa -> {
                pessoaMapper.partialUpdate(existingPessoa, pessoaDTO);

                return existingPessoa;
            })
            .flatMap(pessoaRepository::save)
            .map(pessoaMapper::toDto);
    }

    /**
     * Get all the pessoas.
     *
     * @param pageable the pagination information.
     * @return the list of entities.
     */
    @Transactional(readOnly = true)
    public Flux<PessoaDTO> findAll(Pageable pageable) {
        log.debug("Request to get all Pessoas");
        return pessoaRepository.findAllBy(pageable).map(pessoaMapper::toDto);
    }

    /**
     * Find pessoas by Criteria.
     *
     * @param pageable the pagination information.
     * @return the list of entities.
     */
    @Transactional(readOnly = true)
    public Flux<PessoaDTO> findByCriteria(PessoaCriteria criteria, Pageable pageable) {
        log.debug("Request to get all Pessoas by Criteria");
        return pessoaRepository.findByCriteria(criteria, pageable);
    }

    /**
     * Find the count of pessoas by criteria.
     * @param criteria filtering criteria
     * @return the count of pessoas
     */
    public Mono<Long> countByCriteria(PessoaCriteria criteria) {
        log.debug("Request to get the count of all Pessoas by Criteria");
        return pessoaRepository.countByCriteria(criteria);
    }

    /**
     * Returns the number of pessoas available.
     * @return the number of entities in the database.
     *
     */
    public Mono<Long> countAll() {
        return pessoaRepository.count();
    }

    /**
     * Get one pessoa by id.
     *
     * @param id the id of the entity.
     * @return the entity.
     */
    @Transactional(readOnly = true)
    public Mono<PessoaDTO> findOne(Long id) {
        log.debug("Request to get Pessoa : {}", id);
        return pessoaRepository.findById(id).map(pessoaMapper::toDto);
    }

    /**
     * Delete the pessoa by id.
     *
     * @param id the id of the entity.
     * @return a Mono to signal the deletion
     */
    public Mono<Void> delete(Long id) {
        log.debug("Request to delete Pessoa : {}", id);
        return pessoaRepository.deleteById(id);
    }
}
