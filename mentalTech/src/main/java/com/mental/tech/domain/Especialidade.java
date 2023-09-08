package com.mental.tech.domain;

import jakarta.validation.constraints.*;
import java.io.Serializable;
import org.springframework.data.annotation.Id;
import org.springframework.data.relational.core.mapping.Column;
import org.springframework.data.relational.core.mapping.Table;

/**
 * A Especialidade.
 */
@Table("especialidade")
@SuppressWarnings("common-java:DuplicatedBlocks")
public class Especialidade implements Serializable {

    private static final long serialVersionUID = 1L;

    @Id
    @Column("id")
    private Long id;

    @NotNull(message = "must not be null")
    @Column("id_especialidade")
    private Integer idEspecialidade;

    @Size(max = 150)
    @Column("nome_especialidade")
    private String nomeEspecialidade;

    // jhipster-needle-entity-add-field - JHipster will add fields here

    public Long getId() {
        return this.id;
    }

    public Especialidade id(Long id) {
        this.setId(id);
        return this;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Integer getIdEspecialidade() {
        return this.idEspecialidade;
    }

    public Especialidade idEspecialidade(Integer idEspecialidade) {
        this.setIdEspecialidade(idEspecialidade);
        return this;
    }

    public void setIdEspecialidade(Integer idEspecialidade) {
        this.idEspecialidade = idEspecialidade;
    }

    public String getNomeEspecialidade() {
        return this.nomeEspecialidade;
    }

    public Especialidade nomeEspecialidade(String nomeEspecialidade) {
        this.setNomeEspecialidade(nomeEspecialidade);
        return this;
    }

    public void setNomeEspecialidade(String nomeEspecialidade) {
        this.nomeEspecialidade = nomeEspecialidade;
    }

    // jhipster-needle-entity-add-getters-setters - JHipster will add getters and setters here

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (!(o instanceof Especialidade)) {
            return false;
        }
        return id != null && id.equals(((Especialidade) o).id);
    }

    @Override
    public int hashCode() {
        // see https://vladmihalcea.com/how-to-implement-equals-and-hashcode-using-the-jpa-entity-identifier/
        return getClass().hashCode();
    }

    // prettier-ignore
    @Override
    public String toString() {
        return "Especialidade{" +
            "id=" + getId() +
            ", idEspecialidade=" + getIdEspecialidade() +
            ", nomeEspecialidade='" + getNomeEspecialidade() + "'" +
            "}";
    }
}
