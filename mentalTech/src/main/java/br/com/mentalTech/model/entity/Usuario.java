package br.com.mentalTech.model.entity;

import jakarta.persistence.*;
import lombok.Data;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDate;

@Entity
@Data
@Getter@Setter
public class Usuario {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(nullable = false, length = 150)
    private  String nome;

    @Column(nullable = false)
    private  LocalDate dataNascimento;
    @Column(nullable = false, length = 150)
    private  String email;

    @Column(nullable = false)
    private Long telefone;
    @Column(nullable = false)
    private String senha;
    @Column(length = 150)
    private LocalDate dataCadastro;


}
