import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PrincipalComponent } from './views/principal/principal.component';
import { EntrarComponent } from './views/entrar/entrar.component';
import { EscolhaPerfilComponent } from './views/escolha-perfil/escolha-perfil.component';
import { CadastroPacienteComponent } from './views/cadastro-paciente/cadastro-paciente.component';
import { CadastroProfissionalComponent } from './views/cadastro-profissional/cadastro-profissional.component';
import { SobreComponent } from './views/sobre/sobre.component';
import { SouProfissionalComponent } from './views/sou-profissional/sou-profissional.component';
import { EspecialistasComponent } from './views/especialistas/especialistas.component';
import { CadastroEspEndTemComponent } from './views/cadastro-esp-end-tem/cadastro-esp-end-tem.component';

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
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
