package com.mental.tech.repository.rowmapper;

import com.mental.tech.domain.Pessoa;
import com.mental.tech.domain.enumeration.sexoEnum;
import io.r2dbc.spi.Row;
import java.time.LocalDate;
import java.util.function.BiFunction;
import org.springframework.stereotype.Service;

/**
 * Converter between {@link Row} to {@link Pessoa}, with proper type conversions.
 */
@Service
public class PessoaRowMapper implements BiFunction<Row, String, Pessoa> {

    private final ColumnConverter converter;

    public PessoaRowMapper(ColumnConverter converter) {
        this.converter = converter;
    }

    /**
     * Take a {@link Row} and a column prefix, and extract all the fields.
     * @return the {@link Pessoa} stored in the database.
     */
    @Override
    public Pessoa apply(Row row, String prefix) {
        Pessoa entity = new Pessoa();
        entity.setId(converter.fromRow(row, prefix + "_id", Long.class));
        entity.setIdPessoa(converter.fromRow(row, prefix + "_id_pessoa", Integer.class));
        entity.setNome(converter.fromRow(row, prefix + "_nome", String.class));
        entity.setDataNascimento(converter.fromRow(row, prefix + "_data_nascimento", LocalDate.class));
        entity.setEmail(converter.fromRow(row, prefix + "_email", String.class));
        entity.setSexo(converter.fromRow(row, prefix + "_sexo", sexoEnum.class));
        entity.setTelefone(converter.fromRow(row, prefix + "_telefone", Integer.class));
        entity.setSenha(converter.fromRow(row, prefix + "_senha", String.class));
        return entity;
    }
}
