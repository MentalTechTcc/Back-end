package com.mental.tech.service.dto;

import com.mental.tech.domain.enumeration.sexoEnum;
import jakarta.validation.constraints.*;
import java.io.Serializable;
import java.time.LocalDate;
import java.util.Objects;

/**
 * A DTO for the {@link com.mental.tech.domain.Pessoa} entity.
 */
@SuppressWarnings("common-java:DuplicatedBlocks")
public class PessoaDTO implements Serializable {

    private Long id;

    @NotNull(message = "must not be null")
    private Integer idPessoa;

    @Size(max = 250)
    private String nome;

    @NotNull(message = "must not be null")
    private LocalDate dataNascimento;

    @NotNull(message = "must not be null")
    private String email;

    @NotNull(message = "must not be null")
    private sexoEnum sexo;

    @Max(value = 15)
    private Integer telefone;

    private String senha;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Integer getIdPessoa() {
        return idPessoa;
    }

    public void setIdPessoa(Integer idPessoa) {
        this.idPessoa = idPessoa;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public LocalDate getDataNascimento() {
        return dataNascimento;
    }

    public void setDataNascimento(LocalDate dataNascimento) {
        this.dataNascimento = dataNascimento;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public sexoEnum getSexo() {
        return sexo;
    }

    public void setSexo(sexoEnum sexo) {
        this.sexo = sexo;
    }

    public Integer getTelefone() {
        return telefone;
    }

    public void setTelefone(Integer telefone) {
        this.telefone = telefone;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (!(o instanceof PessoaDTO)) {
            return false;
        }

        PessoaDTO pessoaDTO = (PessoaDTO) o;
        if (this.id == null) {
            return false;
        }
        return Objects.equals(this.id, pessoaDTO.id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.id);
    }

    // prettier-ignore
    @Override
    public String toString() {
        return "PessoaDTO{" +
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
