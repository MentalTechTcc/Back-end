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
import { MeusDadosProfissionalComponent } from './views/profissional/meus-dados/meus-dados.component-profissional';
import { MeusDadosPacienteComponent } from './views/paciente/meus-dados-paciente/meus-dados-paciente.component';
import { ListarProfissionaisComponent } from './views/paciente/listar-profissionais/listar-profissionais.component';
import { DicasPacienteComponent } from './views/paciente/dicas-paciente/dicas-paciente.component';
import { DicaProfissionalComponent } from './views/profissional/dica-profissional/dica-profissional.component';
import { CadastroAgendaProfissionalComponent } from './views/profissional/cadastro-agenda-profissional/cadastro-agenda-profissional.component';
import { JitsiComponent } from './views/jitsi-integration/jitsi-integration.component';
import { AvaliacaoPacienteComponent } from './views/paciente/avaliacao-paciente/avaliacao-paciente.component';
import { MinhaAgendaProfissionalComponent } from './views/profissional/minha-agenda-profissional/minha-agenda-profissional.component';
import {AgendaModalComponent}from './views/paciente/agenda-modal/agenda-modal.component';
import {MinhasConsultasComponent} from './views/paciente/minhas-consultas/minhas-consultas.component'
import { PagamentoComponent } from './views/paciente/pagamento/pagamento.component';
import { EducacionalComponent } from './views/profissional/educacional/educacional.component';
import { MeusPacientesComponent } from './views/profissional/meus-pacientes/meus-pacientes.component'
import { RelatoriosPacienteComponent } from './views/profissional/relatorios-paciente/relatorios-paciente.component'

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
    component: MeusDadosProfissionalComponent
  },
  {
    path: 'meus-dados-paciente',
    component: MeusDadosPacienteComponent
  },
  {
    path: 'listar-profissionais',
    component: ListarProfissionaisComponent
  },
  {
    path: 'dicas-paciente',
    component: DicasPacienteComponent
  },
  {
    path: 'dica-profissional',
    component: DicaProfissionalComponent
  },
  {
    path: 'agenda-profissional',
    component: CadastroAgendaProfissionalComponent
  },
  {
    path: 'home-entrar-profissional',
    component: HomeEntrarProfissionalComponent
  },
  {
    path: 'jitsi',
    component: JitsiComponent
  },
  {
    path: 'avaliacao',
    component: AvaliacaoPacienteComponent
  },
  {
    path: 'minha-agenda',
    component: MinhaAgendaProfissionalComponent
  },
  {
    path: 'agenda-modal',
    component: AgendaModalComponent
  },
  {
    path: 'minhas-consultas',
    component: MinhasConsultasComponent
  },
  {
    path: 'pagamento',
    component: PagamentoComponent
  },
  {
    path: 'educacional',
    component: EducacionalComponent
  }
  ,
  {
    path: 'meus-pacientes',
    component: MeusPacientesComponent
  },
  {
    path: 'relatorios-paciente/:idPessoa/:cpfProfissional',
    component:RelatoriosPacienteComponent
  }
 

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
