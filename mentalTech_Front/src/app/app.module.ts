import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CabecalhoComponent } from './views/cabecalho/cabecalho.component';
import { RodapeComponent } from './views/rodape/rodape.component';
import { PrincipalComponent } from './views/principal/principal.component';
import { EntrarComponent } from './views/entrar/entrar.component';
import { EscolhaPerfilComponent } from './views/escolha-perfil/escolha-perfil.component';
import { CadastroComponent } from './views/cadastro/cadastro.component';
import { CadastroUsuarioService } from './services/cadastro-usuario.service';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    CabecalhoComponent,
    RodapeComponent,
    PrincipalComponent,
    EntrarComponent,
    EscolhaPerfilComponent,
    CadastroComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [CadastroUsuarioService],
  bootstrap: [AppComponent]
})
export class AppModule { }
