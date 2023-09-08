import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';

@NgModule({
  imports: [
    RouterModule.forChild([
      {
        path: 'especialidade',
        data: { pageTitle: 'mentalTechApp.especialidade.home.title' },
        loadChildren: () => import('./especialidade/especialidade.routes'),
      },
      {
        path: 'pessoa',
        data: { pageTitle: 'mentalTechApp.pessoa.home.title' },
        loadChildren: () => import('./pessoa/pessoa.routes'),
      },
      /* jhipster-needle-add-entity-route - JHipster will add entity modules routes here */
    ]),
  ],
})
export class EntityRoutingModule {}
