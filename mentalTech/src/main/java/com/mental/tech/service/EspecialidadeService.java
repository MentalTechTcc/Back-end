package com.mental.tech.service;

import com.mental.tech.domain.Especialidade;
import com.mental.tech.domain.criteria.EspecialidadeCriteria;
import com.mental.tech.repository.EspecialidadeRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

/**
 * Service Implementation for managing {@link Especialidade}.
 */
@Service
@Transactional
public class EspecialidadeService {

    private final Logger log = LoggerFactory.getLogger(EspecialidadeService.class);

    private final EspecialidadeRepository especialidadeRepository;

    public EspecialidadeService(EspecialidadeRepository especialidadeRepository) {
        this.especialidadeRepository = especialidadeRepository;
    }

    /**
     * Save a especialidade.
     *
     * @param especialidade the entity to save.
     * @return the persisted entity.
     */
    public Mono<Especialidade> save(Especialidade especialidade) {
        log.debug("Request to save Especialidade : {}", especialidade);
        return especialidadeRepository.save(especialidade);
    }

    /**
     * Update a especialidade.
     *
     * @param especialidade the entity to save.
     * @return the persisted entity.
     */
    public Mono<Especialidade> update(Especialidade especialidade) {
        log.debug("Request to update Especialidade : {}", especialidade);
        return especialidadeRepository.save(especialidade);
    }

    /**
     * Partially update a especialidade.
     *
     * @param especialidade the entity to update partially.
     * @return the persisted entity.
     */
    public Mono<Especialidade> partialUpdate(Especialidade especialidade) {
        log.debug("Request to partially update Especialidade : {}", especialidade);

        return especialidadeRepository
            .findById(especialidade.getId())
            .map(existingEspecialidade -> {
                if (especialidade.getIdEspecialidade() != null) {
                    existingEspecialidade.setIdEspecialidade(especialidade.getIdEspecialidade());
                }
                if (especialidade.getNomeEspecialidade() != null) {
                    existingEspecialidade.setNomeEspecialidade(especialidade.getNomeEspecialidade());
                }

                return existingEspecialidade;
            })
            .flatMap(especialidadeRepository::save);
    }

    /**
     * Get all the especialidades.
     *
     * @param pageable the pagination information.
     * @return the list of entities.
     */
    @Transactional(readOnly = true)
    public Flux<Especialidade> findAll(Pageable pageable) {
        log.debug("Request to get all Especialidades");
        return especialidadeRepository.findAllBy(pageable);
    }

    /**
     * Find especialidades by Criteria.
     *
     * @param pageable the pagination information.
     * @return the list of entities.
     */
    @Transactional(readOnly = true)
    public Flux<Especialidade> findByCriteria(EspecialidadeCriteria criteria, Pageable pageable) {
        log.debug("Request to get all Especialidades by Criteria");
        return especialidadeRepository.findByCriteria(criteria, pageable);
    }

    /**
     * Find the count of especialidades by criteria.
     * @param criteria filtering criteria
     * @return the count of especialidades
     */
    public Mono<Long> countByCriteria(EspecialidadeCriteria criteria) {
        log.debug("Request to get the count of all Especialidades by Criteria");
        return especialidadeRepository.countByCriteria(criteria);
    }

    /**
     * Returns the number of especialidades available.
     * @return the number of entities in the database.
     *
     */
    public Mono<Long> countAll() {
        return especialidadeRepository.count();
    }

    /**
     * Get one especialidade by id.
     *
     * @param id the id of the entity.
     * @return the entity.
     */
    @Transactional(readOnly = true)
    public Mono<Especialidade> findOne(Long id) {
        log.debug("Request to get Especialidade : {}", id);
        return especialidadeRepository.findById(id);
    }

    /**
     * Delete the especialidade by id.
     *
     * @param id the id of the entity.
     * @return a Mono to signal the deletion
     */
    public Mono<Void> delete(Long id) {
        log.debug("Request to delete Especialidade : {}", id);
        return especialidadeRepository.deleteById(id);
    }
}
