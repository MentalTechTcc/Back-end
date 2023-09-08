package com.mental.tech.web.rest;

import com.mental.tech.domain.Especialidade;
import com.mental.tech.domain.criteria.EspecialidadeCriteria;
import com.mental.tech.repository.EspecialidadeRepository;
import com.mental.tech.service.EspecialidadeService;
import com.mental.tech.web.rest.errors.BadRequestAlertException;
import jakarta.validation.Valid;
import jakarta.validation.constraints.NotNull;
import java.net.URI;
import java.net.URISyntaxException;
import java.util.List;
import java.util.Objects;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.data.domain.PageImpl;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.http.server.reactive.ServerHttpRequest;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;
import org.springframework.web.util.UriComponentsBuilder;
import reactor.core.publisher.Mono;
import tech.jhipster.web.util.HeaderUtil;
import tech.jhipster.web.util.PaginationUtil;
import tech.jhipster.web.util.reactive.ResponseUtil;

/**
 * REST controller for managing {@link com.mental.tech.domain.Especialidade}.
 */
@RestController
@RequestMapping("/api")
public class EspecialidadeResource {

    private final Logger log = LoggerFactory.getLogger(EspecialidadeResource.class);

    private static final String ENTITY_NAME = "especialidade";

    @Value("${jhipster.clientApp.name}")
    private String applicationName;

    private final EspecialidadeService especialidadeService;

    private final EspecialidadeRepository especialidadeRepository;

    public EspecialidadeResource(EspecialidadeService especialidadeService, EspecialidadeRepository especialidadeRepository) {
        this.especialidadeService = especialidadeService;
        this.especialidadeRepository = especialidadeRepository;
    }

    /**
     * {@code POST  /especialidades} : Create a new especialidade.
     *
     * @param especialidade the especialidade to create.
     * @return the {@link ResponseEntity} with status {@code 201 (Created)} and with body the new especialidade, or with status {@code 400 (Bad Request)} if the especialidade has already an ID.
     * @throws URISyntaxException if the Location URI syntax is incorrect.
     */
    @PostMapping("/especialidades")
    public Mono<ResponseEntity<Especialidade>> createEspecialidade(@Valid @RequestBody Especialidade especialidade)
        throws URISyntaxException {
        log.debug("REST request to save Especialidade : {}", especialidade);
        if (especialidade.getId() != null) {
            throw new BadRequestAlertException("A new especialidade cannot already have an ID", ENTITY_NAME, "idexists");
        }
        return especialidadeService
            .save(especialidade)
            .map(result -> {
                try {
                    return ResponseEntity
                        .created(new URI("/api/especialidades/" + result.getId()))
                        .headers(HeaderUtil.createEntityCreationAlert(applicationName, true, ENTITY_NAME, result.getId().toString()))
                        .body(result);
                } catch (URISyntaxException e) {
                    throw new RuntimeException(e);
                }
            });
    }

    /**
     * {@code PUT  /especialidades/:id} : Updates an existing especialidade.
     *
     * @param id the id of the especialidade to save.
     * @param especialidade the especialidade to update.
     * @return the {@link ResponseEntity} with status {@code 200 (OK)} and with body the updated especialidade,
     * or with status {@code 400 (Bad Request)} if the especialidade is not valid,
     * or with status {@code 500 (Internal Server Error)} if the especialidade couldn't be updated.
     * @throws URISyntaxException if the Location URI syntax is incorrect.
     */
    @PutMapping("/especialidades/{id}")
    public Mono<ResponseEntity<Especialidade>> updateEspecialidade(
        @PathVariable(value = "id", required = false) final Long id,
        @Valid @RequestBody Especialidade especialidade
    ) throws URISyntaxException {
        log.debug("REST request to update Especialidade : {}, {}", id, especialidade);
        if (especialidade.getId() == null) {
            throw new BadRequestAlertException("Invalid id", ENTITY_NAME, "idnull");
        }
        if (!Objects.equals(id, especialidade.getId())) {
            throw new BadRequestAlertException("Invalid ID", ENTITY_NAME, "idinvalid");
        }

        return especialidadeRepository
            .existsById(id)
            .flatMap(exists -> {
                if (!exists) {
                    return Mono.error(new BadRequestAlertException("Entity not found", ENTITY_NAME, "idnotfound"));
                }

                return especialidadeService
                    .update(especialidade)
                    .switchIfEmpty(Mono.error(new ResponseStatusException(HttpStatus.NOT_FOUND)))
                    .map(result ->
                        ResponseEntity
                            .ok()
                            .headers(HeaderUtil.createEntityUpdateAlert(applicationName, true, ENTITY_NAME, result.getId().toString()))
                            .body(result)
                    );
            });
    }

    /**
     * {@code PATCH  /especialidades/:id} : Partial updates given fields of an existing especialidade, field will ignore if it is null
     *
     * @param id the id of the especialidade to save.
     * @param especialidade the especialidade to update.
     * @return the {@link ResponseEntity} with status {@code 200 (OK)} and with body the updated especialidade,
     * or with status {@code 400 (Bad Request)} if the especialidade is not valid,
     * or with status {@code 404 (Not Found)} if the especialidade is not found,
     * or with status {@code 500 (Internal Server Error)} if the especialidade couldn't be updated.
     * @throws URISyntaxException if the Location URI syntax is incorrect.
     */
    @PatchMapping(value = "/especialidades/{id}", consumes = { "application/json", "application/merge-patch+json" })
    public Mono<ResponseEntity<Especialidade>> partialUpdateEspecialidade(
        @PathVariable(value = "id", required = false) final Long id,
        @NotNull @RequestBody Especialidade especialidade
    ) throws URISyntaxException {
        log.debug("REST request to partial update Especialidade partially : {}, {}", id, especialidade);
        if (especialidade.getId() == null) {
            throw new BadRequestAlertException("Invalid id", ENTITY_NAME, "idnull");
        }
        if (!Objects.equals(id, especialidade.getId())) {
            throw new BadRequestAlertException("Invalid ID", ENTITY_NAME, "idinvalid");
        }

        return especialidadeRepository
            .existsById(id)
            .flatMap(exists -> {
                if (!exists) {
                    return Mono.error(new BadRequestAlertException("Entity not found", ENTITY_NAME, "idnotfound"));
                }

                Mono<Especialidade> result = especialidadeService.partialUpdate(especialidade);

                return result
                    .switchIfEmpty(Mono.error(new ResponseStatusException(HttpStatus.NOT_FOUND)))
                    .map(res ->
                        ResponseEntity
                            .ok()
                            .headers(HeaderUtil.createEntityUpdateAlert(applicationName, true, ENTITY_NAME, res.getId().toString()))
                            .body(res)
                    );
            });
    }

    /**
     * {@code GET  /especialidades} : get all the especialidades.
     *
     * @param pageable the pagination information.
     * @param request a {@link ServerHttpRequest} request.
     * @param criteria the criteria which the requested entities should match.
     * @return the {@link ResponseEntity} with status {@code 200 (OK)} and the list of especialidades in body.
     */
    @GetMapping(value = "/especialidades", produces = MediaType.APPLICATION_JSON_VALUE)
    public Mono<ResponseEntity<List<Especialidade>>> getAllEspecialidades(
        EspecialidadeCriteria criteria,
        @org.springdoc.core.annotations.ParameterObject Pageable pageable,
        ServerHttpRequest request
    ) {
        log.debug("REST request to get Especialidades by criteria: {}", criteria);
        return especialidadeService
            .countByCriteria(criteria)
            .zipWith(especialidadeService.findByCriteria(criteria, pageable).collectList())
            .map(countWithEntities ->
                ResponseEntity
                    .ok()
                    .headers(
                        PaginationUtil.generatePaginationHttpHeaders(
                            UriComponentsBuilder.fromHttpRequest(request),
                            new PageImpl<>(countWithEntities.getT2(), pageable, countWithEntities.getT1())
                        )
                    )
                    .body(countWithEntities.getT2())
            );
    }

    /**
     * {@code GET  /especialidades/count} : count all the especialidades.
     *
     * @param criteria the criteria which the requested entities should match.
     * @return the {@link ResponseEntity} with status {@code 200 (OK)} and the count in body.
     */
    @GetMapping("/especialidades/count")
    public Mono<ResponseEntity<Long>> countEspecialidades(EspecialidadeCriteria criteria) {
        log.debug("REST request to count Especialidades by criteria: {}", criteria);
        return especialidadeService.countByCriteria(criteria).map(count -> ResponseEntity.status(HttpStatus.OK).body(count));
    }

    /**
     * {@code GET  /especialidades/:id} : get the "id" especialidade.
     *
     * @param id the id of the especialidade to retrieve.
     * @return the {@link ResponseEntity} with status {@code 200 (OK)} and with body the especialidade, or with status {@code 404 (Not Found)}.
     */
    @GetMapping("/especialidades/{id}")
    public Mono<ResponseEntity<Especialidade>> getEspecialidade(@PathVariable Long id) {
        log.debug("REST request to get Especialidade : {}", id);
        Mono<Especialidade> especialidade = especialidadeService.findOne(id);
        return ResponseUtil.wrapOrNotFound(especialidade);
    }

    /**
     * {@code DELETE  /especialidades/:id} : delete the "id" especialidade.
     *
     * @param id the id of the especialidade to delete.
     * @return the {@link ResponseEntity} with status {@code 204 (NO_CONTENT)}.
     */
    @DeleteMapping("/especialidades/{id}")
    public Mono<ResponseEntity<Void>> deleteEspecialidade(@PathVariable Long id) {
        log.debug("REST request to delete Especialidade : {}", id);
        return especialidadeService
            .delete(id)
            .then(
                Mono.just(
                    ResponseEntity
                        .noContent()
                        .headers(HeaderUtil.createEntityDeletionAlert(applicationName, true, ENTITY_NAME, id.toString()))
                        .build()
                )
            );
    }
}
