package com.mental.tech.domain.criteria;

import com.mental.tech.domain.enumeration.sexoEnum;
import java.io.Serializable;
import java.util.Objects;
import org.springdoc.core.annotations.ParameterObject;
import tech.jhipster.service.Criteria;
import tech.jhipster.service.filter.*;

/**
 * Criteria class for the {@link com.mental.tech.domain.Pessoa} entity. This class is used
 * in {@link com.mental.tech.web.rest.PessoaResource} to receive all the possible filtering options from
 * the Http GET request parameters.
 * For example the following could be a valid request:
 * {@code /pessoas?id.greaterThan=5&attr1.contains=something&attr2.specified=false}
 * As Spring is unable to properly convert the types, unless specific {@link Filter} class are used, we need to use
 * fix type specific filters.
 */
@ParameterObject
@SuppressWarnings("common-java:DuplicatedBlocks")
public class PessoaCriteria implements Serializable, Criteria {

    /**
     * Class for filtering sexoEnum
     */
    public static class sexoEnumFilter extends Filter<sexoEnum> {

        public sexoEnumFilter() {}

        public sexoEnumFilter(sexoEnumFilter filter) {
            super(filter);
        }

        @Override
        public sexoEnumFilter copy() {
            return new sexoEnumFilter(this);
        }
    }

    private static final long serialVersionUID = 1L;

    private LongFilter id;

    private IntegerFilter idPessoa;

    private StringFilter nome;

    private LocalDateFilter dataNascimento;

    private StringFilter email;

    private sexoEnumFilter sexo;

    private IntegerFilter telefone;

    private StringFilter senha;

    private Boolean distinct;

    public PessoaCriteria() {}

    public PessoaCriteria(PessoaCriteria other) {
        this.id = other.id == null ? null : other.id.copy();
        this.idPessoa = other.idPessoa == null ? null : other.idPessoa.copy();
        this.nome = other.nome == null ? null : other.nome.copy();
        this.dataNascimento = other.dataNascimento == null ? null : other.dataNascimento.copy();
        this.email = other.email == null ? null : other.email.copy();
        this.sexo = other.sexo == null ? null : other.sexo.copy();
        this.telefone = other.telefone == null ? null : other.telefone.copy();
        this.senha = other.senha == null ? null : other.senha.copy();
        this.distinct = other.distinct;
    }

    @Override
    public PessoaCriteria copy() {
        return new PessoaCriteria(this);
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

    public IntegerFilter getIdPessoa() {
        return idPessoa;
    }

    public IntegerFilter idPessoa() {
        if (idPessoa == null) {
            idPessoa = new IntegerFilter();
        }
        return idPessoa;
    }

    public void setIdPessoa(IntegerFilter idPessoa) {
        this.idPessoa = idPessoa;
    }

    public StringFilter getNome() {
        return nome;
    }

    public StringFilter nome() {
        if (nome == null) {
            nome = new StringFilter();
        }
        return nome;
    }

    public void setNome(StringFilter nome) {
        this.nome = nome;
    }

    public LocalDateFilter getDataNascimento() {
        return dataNascimento;
    }

    public LocalDateFilter dataNascimento() {
        if (dataNascimento == null) {
            dataNascimento = new LocalDateFilter();
        }
        return dataNascimento;
    }

    public void setDataNascimento(LocalDateFilter dataNascimento) {
        this.dataNascimento = dataNascimento;
    }

    public StringFilter getEmail() {
        return email;
    }

    public StringFilter email() {
        if (email == null) {
            email = new StringFilter();
        }
        return email;
    }

    public void setEmail(StringFilter email) {
        this.email = email;
    }

    public sexoEnumFilter getSexo() {
        return sexo;
    }

    public sexoEnumFilter sexo() {
        if (sexo == null) {
            sexo = new sexoEnumFilter();
        }
        return sexo;
    }

    public void setSexo(sexoEnumFilter sexo) {
        this.sexo = sexo;
    }

    public IntegerFilter getTelefone() {
        return telefone;
    }

    public IntegerFilter telefone() {
        if (telefone == null) {
            telefone = new IntegerFilter();
        }
        return telefone;
    }

    public void setTelefone(IntegerFilter telefone) {
        this.telefone = telefone;
    }

    public StringFilter getSenha() {
        return senha;
    }

    public StringFilter senha() {
        if (senha == null) {
            senha = new StringFilter();
        }
        return senha;
    }

    public void setSenha(StringFilter senha) {
        this.senha = senha;
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
        final PessoaCriteria that = (PessoaCriteria) o;
        return (
            Objects.equals(id, that.id) &&
            Objects.equals(idPessoa, that.idPessoa) &&
            Objects.equals(nome, that.nome) &&
            Objects.equals(dataNascimento, that.dataNascimento) &&
            Objects.equals(email, that.email) &&
            Objects.equals(sexo, that.sexo) &&
            Objects.equals(telefone, that.telefone) &&
            Objects.equals(senha, that.senha) &&
            Objects.equals(distinct, that.distinct)
        );
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, idPessoa, nome, dataNascimento, email, sexo, telefone, senha, distinct);
    }

    // prettier-ignore
    @Override
    public String toString() {
        return "PessoaCriteria{" +
            (id != null ? "id=" + id + ", " : "") +
            (idPessoa != null ? "idPessoa=" + idPessoa + ", " : "") +
            (nome != null ? "nome=" + nome + ", " : "") +
            (dataNascimento != null ? "dataNascimento=" + dataNascimento + ", " : "") +
            (email != null ? "email=" + email + ", " : "") +
            (sexo != null ? "sexo=" + sexo + ", " : "") +
            (telefone != null ? "telefone=" + telefone + ", " : "") +
            (senha != null ? "senha=" + senha + ", " : "") +
            (distinct != null ? "distinct=" + distinct + ", " : "") +
            "}";
    }
}
