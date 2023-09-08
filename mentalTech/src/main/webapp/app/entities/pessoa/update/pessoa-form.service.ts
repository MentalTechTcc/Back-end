import { Injectable } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';

import { IPessoa, NewPessoa } from '../pessoa.model';

/**
 * A partial Type with required key is used as form input.
 */
type PartialWithRequiredKeyOf<T extends { id: unknown }> = Partial<Omit<T, 'id'>> & { id: T['id'] };

/**
 * Type for createFormGroup and resetForm argument.
 * It accepts IPessoa for edit and NewPessoaFormGroupInput for create.
 */
type PessoaFormGroupInput = IPessoa | PartialWithRequiredKeyOf<NewPessoa>;

type PessoaFormDefaults = Pick<NewPessoa, 'id'>;

type PessoaFormGroupContent = {
  id: FormControl<IPessoa['id'] | NewPessoa['id']>;
  idPessoa: FormControl<IPessoa['idPessoa']>;
  nome: FormControl<IPessoa['nome']>;
  dataNascimento: FormControl<IPessoa['dataNascimento']>;
  email: FormControl<IPessoa['email']>;
  sexo: FormControl<IPessoa['sexo']>;
  telefone: FormControl<IPessoa['telefone']>;
  senha: FormControl<IPessoa['senha']>;
};

export type PessoaFormGroup = FormGroup<PessoaFormGroupContent>;

@Injectable({ providedIn: 'root' })
export class PessoaFormService {
  createPessoaFormGroup(pessoa: PessoaFormGroupInput = { id: null }): PessoaFormGroup {
    const pessoaRawValue = {
      ...this.getFormDefaults(),
      ...pessoa,
    };
    return new FormGroup<PessoaFormGroupContent>({
      id: new FormControl(
        { value: pessoaRawValue.id, disabled: true },
        {
          nonNullable: true,
          validators: [Validators.required],
        }
      ),
      idPessoa: new FormControl(pessoaRawValue.idPessoa, {
        validators: [Validators.required],
      }),
      nome: new FormControl(pessoaRawValue.nome, {
        validators: [Validators.maxLength(250)],
      }),
      dataNascimento: new FormControl(pessoaRawValue.dataNascimento, {
        validators: [Validators.required],
      }),
      email: new FormControl(pessoaRawValue.email, {
        validators: [Validators.required],
      }),
      sexo: new FormControl(pessoaRawValue.sexo, {
        validators: [Validators.required],
      }),
      telefone: new FormControl(pessoaRawValue.telefone, {
        validators: [Validators.max(15)],
      }),
      senha: new FormControl(pessoaRawValue.senha),
    });
  }

  getPessoa(form: PessoaFormGroup): IPessoa | NewPessoa {
    return form.getRawValue() as IPessoa | NewPessoa;
  }

  resetForm(form: PessoaFormGroup, pessoa: PessoaFormGroupInput): void {
    const pessoaRawValue = { ...this.getFormDefaults(), ...pessoa };
    form.reset(
      {
        ...pessoaRawValue,
        id: { value: pessoaRawValue.id, disabled: true },
      } as any /* cast to workaround https://github.com/angular/angular/issues/46458 */
    );
  }

  private getFormDefaults(): PessoaFormDefaults {
    return {
      id: null,
    };
  }
}
