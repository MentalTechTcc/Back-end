import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PrincipalComponent } from './views/geral/principal/principal.component';
import { EntrarComponent } from './views/geral/entrar/entrar.component';
import { EscolhaPerfilComponent } from './views/geral/escolha-perfil/escolha-perfil.component';
import { CadastroProfissionalComponent } from './views/profissional/cadastro-profissional/cadastro-profissional.component';
import { SobreComponent } from './views/geral/sobre/sobre.component';
import { SouProfissionalComponent } from './views/geral/sou-profissional/sou-profissional.component';
import { EspecialistasComponent } from './views/geral/especialistas/especialistas.component';
import { CadastroEspEndTemComponent } from './views/profissional/cadastro-esp-end-tem/cadastro-esp-end-tem.component';
import { HomeEntrarProfissionalComponent } from './views/profissional/home-entrar-profissional/home-entrar-profissional.component';
import { CadastroPacienteComponent } from './views/paciente/cadastro-paciente/cadastro-paciente.component';
import { HomePacienteComponent } from './views/paciente/home-paciente/home-paciente.component';
import { MeusDadosComponent } from './views/profissional/meus-dados/meus-dados.component';
import { MeusDadosPacienteComponent } from './views/paciente/meus-dados-paciente/meus-dados-paciente.component';

const routes: Routes = [
  {
    path: '',
    component: PrincipalComponent,
    pathMatch: 'full' // Certifica-se de que é uma correspondência completa
  },
  {
    path: 'home',
    component: PrincipalComponent
  },
  {
    path: 'login',
    component: EntrarComponent
  },
  {
    path: 'escolha-perfil',
    component: EscolhaPerfilComponent
  },
  {
    path: 'cadastro-paciente',
    component: CadastroPacienteComponent
  },
  {
    path: 'cadastro-profissional',
    component: CadastroProfissionalComponent
  },
  {
    path: 'cadastro-profissional-proximo',
    component: CadastroEspEndTemComponent
  },
  {
    path: 'sobre',
    component: SobreComponent
  },
  {
    path: 'sou-profissional',
    component: SouProfissionalComponent
  },
  {
    path: 'especialistas',
    component: EspecialistasComponent
  },
  {
    path: 'home-profissional',
    component: HomeEntrarProfissionalComponent
  },
  {
    path: 'home-paciente',
    component: HomePacienteComponent
  },
  {
    path: 'meus-dados-profissional',
    component: MeusDadosComponent
  },
  {
    path: 'meus-dados-paciente',
    component: MeusDadosPacienteComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
