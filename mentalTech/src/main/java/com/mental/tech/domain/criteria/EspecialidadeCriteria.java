package com.mental.tech.domain.criteria;

import java.io.Serializable;
import java.util.Objects;
import org.springdoc.core.annotations.ParameterObject;
import tech.jhipster.service.Criteria;
import tech.jhipster.service.filter.*;

/**
 * Criteria class for the {@link com.mental.tech.domain.Especialidade} entity. This class is used
 * in {@link com.mental.tech.web.rest.EspecialidadeResource} to receive all the possible filtering options from
 * the Http GET request parameters.
 * For example the following could be a valid request:
 * {@code /especialidades?id.greaterThan=5&attr1.contains=something&attr2.specified=false}
 * As Spring is unable to properly convert the types, unless specific {@link Filter} class are used, we need to use
 * fix type specific filters.
 */
@ParameterObject
@SuppressWarnings("common-java:DuplicatedBlocks")
public class EspecialidadeCriteria implements Serializable, Criteria {

    private static final long serialVersionUID = 1L;

    private LongFilter id;

    private IntegerFilter idEspecialidade;

    private StringFilter nomeEspecialidade;

    private Boolean distinct;

    public EspecialidadeCriteria() {}

    public EspecialidadeCriteria(EspecialidadeCriteria other) {
        this.id = other.id == null ? null : other.id.copy();
        this.idEspecialidade = other.idEspecialidade == null ? null : other.idEspecialidade.copy();
        this.nomeEspecialidade = other.nomeEspecialidade == null ? null : other.nomeEspecialidade.copy();
        this.distinct = other.distinct;
    }

    @Override
    public EspecialidadeCriteria copy() {
        return new EspecialidadeCriteria(this);
    }

    public LongFilter getId() {
        return id;
    }

    public LongFilter id() {
        if (id == null) {
            id = new LongFilter();
        }
        return id;
    }

    public void setId(LongFilter id) {
        this.id = id;
    }

    public IntegerFilter getIdEspecialidade() {
        return idEspecialidade;
    }

    public IntegerFilter idEspecialidade() {
        if (idEspecialidade == null) {
            idEspecialidade = new IntegerFilter();
        }
        return idEspecialidade;
    }

    public void setIdEspecialidade(IntegerFilter idEspecialidade) {
        this.idEspecialidade = idEspecialidade;
    }

    public StringFilter getNomeEspecialidade() {
        return nomeEspecialidade;
    }

    public StringFilter nomeEspecialidade() {
        if (nomeEspecialidade == null) {
            nomeEspecialidade = new StringFilter();
        }
        return nomeEspecialidade;
    }

    public void setNomeEspecialidade(StringFilter nomeEspecialidade) {
        this.nomeEspecialidade = nomeEspecialidade;
    }

    public Boolean getDistinct() {
        return distinct;
    }

    public void setDistinct(Boolean distinct) {
        this.distinct = distinct;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        final EspecialidadeCriteria that = (EspecialidadeCriteria) o;
        return (
            Objects.equals(id, that.id) &&
            Objects.equals(idEspecialidade, that.idEspecialidade) &&
            Objects.equals(nomeEspecialidade, that.nomeEspecialidade) &&
            Objects.equals(distinct, that.distinct)
        );
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, idEspecialidade, nomeEspecialidade, distinct);
    }

    // prettier-ignore
    @Override
    public String toString() {
        return "EspecialidadeCriteria{" +
            (id != null ? "id=" + id + ", " : "") +
            (idEspecialidade != null ? "idEspecialidade=" + idEspecialidade + ", " : "") +
            (nomeEspecialidade != null ? "nomeEspecialidade=" + nomeEspecialidade + ", " : "") +
            (distinct != null ? "distinct=" + distinct + ", " : "") +
            "}";
    }
}
