package br.com.mentalTech.service;

import br.com.mentalTech.model.entity.Usuario;
import br.com.mentalTech.repository.UsuarioRepository;
import org.springframework.stereotype.Service;

@Service
public class UsuarioService {

    private UsuarioRepository repository;

    public UsuarioService(UsuarioRepository repository) {
        this.repository = repository;
    }

    public void salvarUsuario(Usuario usuario){


    }
    public void validarUsuario(Usuario usuario){

    }
}
