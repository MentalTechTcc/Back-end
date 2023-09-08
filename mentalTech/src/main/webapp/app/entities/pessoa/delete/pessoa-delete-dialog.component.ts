import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';

import SharedModule from 'app/shared/shared.module';
import { IPessoa } from '../pessoa.model';
import { PessoaService } from '../service/pessoa.service';
import { ITEM_DELETED_EVENT } from 'app/config/navigation.constants';

@Component({
  standalone: true,
  templateUrl: './pessoa-delete-dialog.component.html',
  imports: [SharedModule, FormsModule],
})
export class PessoaDeleteDialogComponent {
  pessoa?: IPessoa;

  constructor(protected pessoaService: PessoaService, protected activeModal: NgbActiveModal) {}

  cancel(): void {
    this.activeModal.dismiss();
  }

  confirmDelete(id: number): void {
    this.pessoaService.delete(id).subscribe(() => {
      this.activeModal.close(ITEM_DELETED_EVENT);
    });
  }
}
