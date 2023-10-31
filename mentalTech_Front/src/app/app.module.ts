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
import { MeusDadosProfissionalComponent } from './views/profissional/meus-dados/meus-dados.component-profissional';
import { MeusDadosPacienteComponent } from './views/paciente/meus-dados-paciente/meus-dados-paciente.component';
import { ListarProfissionaisComponent } from './views/paciente/listar-profissionais/listar-profissionais.component';
import { DicasPacienteComponent } from './views/paciente/dicas-paciente/dicas-paciente.component';
import { DicaProfissionalComponent } from './views/profissional/dica-profissional/dica-profissional.component';
import { ReactiveFormsModule } from '@angular/forms';
import { CadastroAgendaProfissionalComponent } from './views/profissional/cadastro-agenda-profissional/cadastro-agenda-profissional.component';
import { MinhasConsultasPacienteComponent } from './views/paciente/minhas-consultas-paciente/minhas-consultas-paciente.component';
import { JitsiComponent } from './views/jitsi-integration/jitsi-integration.component';
import { AvaliacaoPacienteComponent } from './views/paciente/avaliacao-paciente/avaliacao-paciente.component';
import { MinhaAgendaProfissionalComponent } from './views/profissional/minha-agenda-profissional/minha-agenda-profissional.component';
import {AgendaModalComponent}from './views/paciente/agenda-modal/agenda-modal.component';
import { MinhasConsultasComponent } from './views/paciente/minhas-consultas/minhas-consultas.component';
import { PagamentoComponent } from './views/paciente/pagamento/pagamento.component';
import { EducacionalComponent } from './views/profissional/educacional/educacional.component';
import { CommonModule } from '@angular/common';


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
    MeusDadosProfissionalComponent,
    MeusDadosPacienteComponent,
    ListarProfissionaisComponent,
    DicasPacienteComponent,
    DicaProfissionalComponent,
    CadastroAgendaProfissionalComponent,
    MinhasConsultasPacienteComponent,
    JitsiComponent,
    AvaliacaoPacienteComponent,
    MinhaAgendaProfissionalComponent,
    AgendaModalComponent,
    MinhasConsultasComponent,
    PagamentoComponent,
    EducacionalComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    MatSnackBarModule,
    HttpClientModule,
    ReactiveFormsModule,
    CommonModule
  ],
  providers: [CadastroUsuarioService, CadastroPacienteService, LoginUsuarioService],
  bootstrap: [AppComponent]
})
export class AppModule { }
