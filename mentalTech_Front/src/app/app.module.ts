import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CabecalhoComponent } from './views/geral/cabecalho/cabecalho.component';
import { RodapeComponent } from './views/geral/rodape/rodape.component';
import { PrincipalComponent } from './views/geral/principal/principal.component';
import { EntrarComponent } from './views/geral/entrar/entrar.component';
import { EscolhaPerfilComponent } from './views/geral/escolha-perfil/escolha-perfil.component';
import { CadastroUsuarioService } from './services/cadastro-usuario.service';
import { FormsModule } from '@angular/forms';
import { MatSnackBarModule } from '@angular/material';
import { CadastroPacienteService } from './services/cadastro-paciente.service';
import { HttpClientModule } from '@angular/common/http';
import { CadastroProfissionalComponent } from './views/profissional/cadastro-profissional/cadastro-profissional.component';
import { SobreComponent } from './views/geral/sobre/sobre.component';
import { SouProfissionalComponent } from './views/geral/sou-profissional/sou-profissional.component';
import { EspecialistasComponent } from './views/geral/especialistas/especialistas.component';
import { CadastroEspEndTemComponent } from './views/profissional/cadastro-esp-end-tem/cadastro-esp-end-tem.component';
import { HomeEntrarProfissionalComponent } from './views/profissional/home-entrar-profissional/home-entrar-profissional.component';
import { CadastroPacienteComponent } from './views/paciente/cadastro-paciente/cadastro-paciente.component';
import { LoginUsuarioService } from './services/login-usuario.service';
import { CabecalhoProfissionalComponent } from './views/profissional/cabecalho-profissional/cabecalho-profissional.component';
import { CabecalhoPacienteComponent } from './views/paciente/cabecalho-paciente/cabecalho-paciente.component';
import { HomePacienteComponent } from './views/paciente/home-paciente/home-paciente.component';
import { MeusDadosComponent } from './views/profissional/meus-dados/meus-dados.component';
import { MeusDadosPacienteComponent } from './views/paciente/meus-dados-paciente/meus-dados-paciente.component';

@NgModule({
  declarations: [
    AppComponent,
    CabecalhoComponent,
    RodapeComponent,
    PrincipalComponent,
    EntrarComponent,
    EscolhaPerfilComponent,
    CadastroPacienteComponent,
    CadastroProfissionalComponent,
    SobreComponent,
    SouProfissionalComponent,
    EspecialistasComponent,
    CadastroEspEndTemComponent,
    HomeEntrarProfissionalComponent,
    CabecalhoProfissionalComponent,
    CabecalhoPacienteComponent,
    HomePacienteComponent,
    MeusDadosComponent,
    MeusDadosPacienteComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    MatSnackBarModule,
    HttpClientModule
  ],
  providers: [CadastroUsuarioService, CadastroPacienteService, LoginUsuarioService],
  bootstrap: [AppComponent]
})
export class AppModule { }
