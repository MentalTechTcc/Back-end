import {
  entityTableSelector,
  entityDetailsButtonSelector,
  entityDetailsBackButtonSelector,
  entityCreateButtonSelector,
  entityCreateSaveButtonSelector,
  entityCreateCancelButtonSelector,
  entityEditButtonSelector,
  entityDeleteButtonSelector,
  entityConfirmDeleteButtonSelector,
} from '../../support/entity';

describe('Pessoa e2e test', () => {
  const pessoaPageUrl = '/pessoa';
  const pessoaPageUrlPattern = new RegExp('/pessoa(\\?.*)?$');
  const username = Cypress.env('E2E_USERNAME') ?? 'user';
  const password = Cypress.env('E2E_PASSWORD') ?? 'user';
  const pessoaSample = { idPessoa: 12981, dataNascimento: '2023-09-08', email: 'Marina_Xavier@yahoo.com', sexo: 'M' };

  let pessoa;

  beforeEach(() => {
    cy.login(username, password);
  });

  beforeEach(() => {
    cy.intercept('GET', '/api/pessoas+(?*|)').as('entitiesRequest');
    cy.intercept('POST', '/api/pessoas').as('postEntityRequest');
    cy.intercept('DELETE', '/api/pessoas/*').as('deleteEntityRequest');
  });

  afterEach(() => {
    if (pessoa) {
      cy.authenticatedRequest({
        method: 'DELETE',
        url: `/api/pessoas/${pessoa.id}`,
      }).then(() => {
        pessoa = undefined;
      });
    }
  });

  it('Pessoas menu should load Pessoas page', () => {
    cy.visit('/');
    cy.clickOnEntityMenuItem('pessoa');
    cy.wait('@entitiesRequest').then(({ response }) => {
      if (response.body.length === 0) {
        cy.get(entityTableSelector).should('not.exist');
      } else {
        cy.get(entityTableSelector).should('exist');
      }
    });
    cy.getEntityHeading('Pessoa').should('exist');
    cy.url().should('match', pessoaPageUrlPattern);
  });

  describe('Pessoa page', () => {
    describe('create button click', () => {
      beforeEach(() => {
        cy.visit(pessoaPageUrl);
        cy.wait('@entitiesRequest');
      });

      it('should load create Pessoa page', () => {
        cy.get(entityCreateButtonSelector).click();
        cy.url().should('match', new RegExp('/pessoa/new$'));
        cy.getEntityCreateUpdateHeading('Pessoa');
        cy.get(entityCreateSaveButtonSelector).should('exist');
        cy.get(entityCreateCancelButtonSelector).click();
        cy.wait('@entitiesRequest').then(({ response }) => {
          expect(response.statusCode).to.equal(200);
        });
        cy.url().should('match', pessoaPageUrlPattern);
      });
    });

    describe('with existing value', () => {
      beforeEach(() => {
        cy.authenticatedRequest({
          method: 'POST',
          url: '/api/pessoas',
          body: pessoaSample,
        }).then(({ body }) => {
          pessoa = body;

          cy.intercept(
            {
              method: 'GET',
              url: '/api/pessoas+(?*|)',
              times: 1,
            },
            {
              statusCode: 200,
              headers: {
                link: '<http://localhost/api/pessoas?page=0&size=20>; rel="last",<http://localhost/api/pessoas?page=0&size=20>; rel="first"',
              },
              body: [pessoa],
            }
          ).as('entitiesRequestInternal');
        });

        cy.visit(pessoaPageUrl);

        cy.wait('@entitiesRequestInternal');
      });

      it('detail button click should load details Pessoa page', () => {
        cy.get(entityDetailsButtonSelector).first().click();
        cy.getEntityDetailsHeading('pessoa');
        cy.get(entityDetailsBackButtonSelector).click();
        cy.wait('@entitiesRequest').then(({ response }) => {
          expect(response.statusCode).to.equal(200);
        });
        cy.url().should('match', pessoaPageUrlPattern);
      });

      it('edit button click should load edit Pessoa page and go back', () => {
        cy.get(entityEditButtonSelector).first().click();
        cy.getEntityCreateUpdateHeading('Pessoa');
        cy.get(entityCreateSaveButtonSelector).should('exist');
        cy.get(entityCreateCancelButtonSelector).click();
        cy.wait('@entitiesRequest').then(({ response }) => {
          expect(response.statusCode).to.equal(200);
        });
        cy.url().should('match', pessoaPageUrlPattern);
      });

      it.skip('edit button click should load edit Pessoa page and save', () => {
        cy.get(entityEditButtonSelector).first().click();
        cy.getEntityCreateUpdateHeading('Pessoa');
        cy.get(entityCreateSaveButtonSelector).click();
        cy.wait('@entitiesRequest').then(({ response }) => {
          expect(response.statusCode).to.equal(200);
        });
        cy.url().should('match', pessoaPageUrlPattern);
      });

      it('last delete button click should delete instance of Pessoa', () => {
        cy.get(entityDeleteButtonSelector).last().click();
        cy.getEntityDeleteDialogHeading('pessoa').should('exist');
        cy.get(entityConfirmDeleteButtonSelector).click();
        cy.wait('@deleteEntityRequest').then(({ response }) => {
          expect(response.statusCode).to.equal(204);
        });
        cy.wait('@entitiesRequest').then(({ response }) => {
          expect(response.statusCode).to.equal(200);
        });
        cy.url().should('match', pessoaPageUrlPattern);

        pessoa = undefined;
      });
    });
  });

  describe('new Pessoa page', () => {
    beforeEach(() => {
      cy.visit(`${pessoaPageUrl}`);
      cy.get(entityCreateButtonSelector).click();
      cy.getEntityCreateUpdateHeading('Pessoa');
    });

    it('should create an instance of Pessoa', () => {
      cy.get(`[data-cy="idPessoa"]`).type('21987');
      cy.get(`[data-cy="idPessoa"]`).should('have.value', '21987');

      cy.get(`[data-cy="nome"]`).type('do Roupas');
      cy.get(`[data-cy="nome"]`).should('have.value', 'do Roupas');

      cy.get(`[data-cy="dataNascimento"]`).type('2023-09-08');
      cy.get(`[data-cy="dataNascimento"]`).blur();
      cy.get(`[data-cy="dataNascimento"]`).should('have.value', '2023-09-08');

      cy.get(`[data-cy="email"]`).type('Felicia.Franco14@hotmail.com');
      cy.get(`[data-cy="email"]`).should('have.value', 'Felicia.Franco14@hotmail.com');

      cy.get(`[data-cy="sexo"]`).select('F');

      cy.get(`[data-cy="telefone"]`).type('10');
      cy.get(`[data-cy="telefone"]`).should('have.value', '10');

      cy.get(`[data-cy="senha"]`).type('Lustroso Tocantins Atentende');
      cy.get(`[data-cy="senha"]`).should('have.value', 'Lustroso Tocantins Atentende');

      cy.get(entityCreateSaveButtonSelector).click();

      cy.wait('@postEntityRequest').then(({ response }) => {
        expect(response.statusCode).to.equal(201);
        pessoa = response.body;
      });
      cy.wait('@entitiesRequest').then(({ response }) => {
        expect(response.statusCode).to.equal(200);
      });
      cy.url().should('match', pessoaPageUrlPattern);
    });
  });
});
