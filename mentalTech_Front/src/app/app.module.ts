import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CabecalhoComponent } from './views/cabecalho/cabecalho.component';
import { RodapeComponent } from './views/rodape/rodape.component';
import { PrincipalComponent } from './views/principal/principal.component';
import { EntrarComponent } from './views/entrar/entrar.component';
import { EscolhaPerfilComponent } from './views/escolha-perfil/escolha-perfil.component';
import { CadastroPacienteComponent } from './views/cadastro-paciente/cadastro-paciente.component';
import { CadastroUsuarioService } from './services/cadastro-usuario.service';
import { FormsModule } from '@angular/forms';
import { MatSnackBarModule } from '@angular/material';
import { CadastroPacienteService } from './services/cadastro-paciente.service';
import { HttpClientModule } from '@angular/common/http';
import { CadastroProfissionalComponent } from './views/cadastro-profissional/cadastro-profissional.component';
import { SobreComponent } from './views/sobre/sobre.component';
import { SouProfissionalComponent } from './views/sou-profissional/sou-profissional.component';
import { EspecialistasComponent } from './views/especialistas/especialistas.component';
import { CadastroEspEndTemComponent } from './views/cadastro-esp-end-tem/cadastro-esp-end-tem.component';

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
    CadastroEspEndTemComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    MatSnackBarModule,
    HttpClientModule
  ],
  providers: [CadastroUsuarioService, CadastroPacienteService],
  bootstrap: [AppComponent]
})
export class AppModule { }
