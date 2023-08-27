package br.com.mentalTech;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;

@Configuration
//@Profile("development")
@Development // anotatton criada
public class MinhaConfiguration {
    /*
    @Bean(name= "applicationName")
    public String applicationName(){
        return "Sistema de Vendas";
    }*/

    @Bean
    public CommandLineRunner executar(){
        return args -> {
            System.out.println("rodando a conf de devel");
        };
    }

}
