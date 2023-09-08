package com.mental.tech.domain;

import com.mental.tech.domain.enumeration.sexoEnum;
import jakarta.validation.constraints.*;
import java.io.Serializable;
import java.time.LocalDate;
import org.springframework.data.annotation.Id;
import org.springframework.data.relational.core.mapping.Column;
import org.springframework.data.relational.core.mapping.Table;

/**
 * A Pessoa.
 */
@Table("pessoa")
@SuppressWarnings("common-java:DuplicatedBlocks")
public class Pessoa implements Serializable {

    private static final long serialVersionUID = 1L;

    @Id
    @Column("id")
    private Long id;

    @NotNull(message = "must not be null")
    @Column("id_pessoa")
    private Integer idPessoa;

    @Size(max = 250)
    @Column("nome")
    private String nome;

    @NotNull(message = "must not be null")
    @Column("data_nascimento")
    private LocalDate dataNascimento;

    @NotNull(message = "must not be null")
    @Column("email")
    private String email;

    @NotNull(message = "must not be null")
    @Column("sexo")
    private sexoEnum sexo;

    @Max(value = 15)
    @Column("telefone")
    private Integer telefone;

    @Column("senha")
    private String senha;

    // jhipster-needle-entity-add-field - JHipster will add fields here

    public Long getId() {
        return this.id;
    }

    public Pessoa id(Long id) {
        this.setId(id);
        return this;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Integer getIdPessoa() {
        return this.idPessoa;
    }

    public Pessoa idPessoa(Integer idPessoa) {
        this.setIdPessoa(idPessoa);
        return this;
    }

    public void setIdPessoa(Integer idPessoa) {
        this.idPessoa = idPessoa;
    }

    public String getNome() {
        return this.nome;
    }

    public Pessoa nome(String nome) {
        this.setNome(nome);
        return this;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public LocalDate getDataNascimento() {
        return this.dataNascimento;
    }

    public Pessoa dataNascimento(LocalDate dataNascimento) {
        this.setDataNascimento(dataNascimento);
        return this;
    }

    public void setDataNascimento(LocalDate dataNascimento) {
        this.dataNascimento = dataNascimento;
    }

    public String getEmail() {
        return this.email;
    }

    public Pessoa email(String email) {
        this.setEmail(email);
        return this;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public sexoEnum getSexo() {
        return this.sexo;
    }

    public Pessoa sexo(sexoEnum sexo) {
        this.setSexo(sexo);
        return this;
    }

    public void setSexo(sexoEnum sexo) {
        this.sexo = sexo;
    }

    public Integer getTelefone() {
        return this.telefone;
    }

    public Pessoa telefone(Integer telefone) {
        this.setTelefone(telefone);
        return this;
    }

    public void setTelefone(Integer telefone) {
        this.telefone = telefone;
    }

    public String getSenha() {
        return this.senha;
    }

    public Pessoa senha(String senha) {
        this.setSenha(senha);
        return this;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    // jhipster-needle-entity-add-getters-setters - JHipster will add getters and setters here

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (!(o instanceof Pessoa)) {
            return false;
        }
        return id != null && id.equals(((Pessoa) o).id);
    }

    @Override
    public int hashCode() {
        // see https://vladmihalcea.com/how-to-implement-equals-and-hashcode-using-the-jpa-entity-identifier/
        return getClass().hashCode();
    }

    // prettier-ignore
    @Override
    public String toString() {
        return "Pessoa{" +
            "id=" + getId() +
            ", idPessoa=" + getIdPessoa() +
            ", nome='" + getNome() + "'" +
            ", dataNascimento='" + getDataNascimento() + "'" +
            ", email='" + getEmail() + "'" +
            ", sexo='" + getSexo() + "'" +
            ", telefone=" + getTelefone() +
            ", senha='" + getSenha() + "'" +
            "}";
    }
}
