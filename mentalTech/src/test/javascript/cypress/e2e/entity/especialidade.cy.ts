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

describe('Especialidade e2e test', () => {
  const especialidadePageUrl = '/especialidade';
  const especialidadePageUrlPattern = new RegExp('/especialidade(\\?.*)?$');
  const username = Cypress.env('E2E_USERNAME') ?? 'user';
  const password = Cypress.env('E2E_PASSWORD') ?? 'user';
  const especialidadeSample = { idEspecialidade: 24098 };

  let especialidade;

  beforeEach(() => {
    cy.login(username, password);
  });

  beforeEach(() => {
    cy.intercept('GET', '/api/especialidades+(?*|)').as('entitiesRequest');
    cy.intercept('POST', '/api/especialidades').as('postEntityRequest');
    cy.intercept('DELETE', '/api/especialidades/*').as('deleteEntityRequest');
  });

  afterEach(() => {
    if (especialidade) {
      cy.authenticatedRequest({
        method: 'DELETE',
        url: `/api/especialidades/${especialidade.id}`,
      }).then(() => {
        especialidade = undefined;
      });
    }
  });

  it('Especialidades menu should load Especialidades page', () => {
    cy.visit('/');
    cy.clickOnEntityMenuItem('especialidade');
    cy.wait('@entitiesRequest').then(({ response }) => {
      if (response.body.length === 0) {
        cy.get(entityTableSelector).should('not.exist');
      } else {
        cy.get(entityTableSelector).should('exist');
      }
    });
    cy.getEntityHeading('Especialidade').should('exist');
    cy.url().should('match', especialidadePageUrlPattern);
  });

  describe('Especialidade page', () => {
    describe('create button click', () => {
      beforeEach(() => {
        cy.visit(especialidadePageUrl);
        cy.wait('@entitiesRequest');
      });

      it('should load create Especialidade page', () => {
        cy.get(entityCreateButtonSelector).click();
        cy.url().should('match', new RegExp('/especialidade/new$'));
        cy.getEntityCreateUpdateHeading('Especialidade');
        cy.get(entityCreateSaveButtonSelector).should('exist');
        cy.get(entityCreateCancelButtonSelector).click();
        cy.wait('@entitiesRequest').then(({ response }) => {
          expect(response.statusCode).to.equal(200);
        });
        cy.url().should('match', especialidadePageUrlPattern);
      });
    });

    describe('with existing value', () => {
      beforeEach(() => {
        cy.authenticatedRequest({
          method: 'POST',
          url: '/api/especialidades',
          body: especialidadeSample,
        }).then(({ body }) => {
          especialidade = body;

          cy.intercept(
            {
              method: 'GET',
              url: '/api/especialidades+(?*|)',
              times: 1,
            },
            {
              statusCode: 200,
              headers: {
                link: '<http://localhost/api/especialidades?page=0&size=20>; rel="last",<http://localhost/api/especialidades?page=0&size=20>; rel="first"',
              },
              body: [especialidade],
            }
          ).as('entitiesRequestInternal');
        });

        cy.visit(especialidadePageUrl);

        cy.wait('@entitiesRequestInternal');
      });

      it('detail button click should load details Especialidade page', () => {
        cy.get(entityDetailsButtonSelector).first().click();
        cy.getEntityDetailsHeading('especialidade');
        cy.get(entityDetailsBackButtonSelector).click();
        cy.wait('@entitiesRequest').then(({ response }) => {
          expect(response.statusCode).to.equal(200);
        });
        cy.url().should('match', especialidadePageUrlPattern);
      });

      it('edit button click should load edit Especialidade page and go back', () => {
        cy.get(entityEditButtonSelector).first().click();
        cy.getEntityCreateUpdateHeading('Especialidade');
        cy.get(entityCreateSaveButtonSelector).should('exist');
        cy.get(entityCreateCancelButtonSelector).click();
        cy.wait('@entitiesRequest').then(({ response }) => {
          expect(response.statusCode).to.equal(200);
        });
        cy.url().should('match', especialidadePageUrlPattern);
      });

      it.skip('edit button click should load edit Especialidade page and save', () => {
        cy.get(entityEditButtonSelector).first().click();
        cy.getEntityCreateUpdateHeading('Especialidade');
        cy.get(entityCreateSaveButtonSelector).click();
        cy.wait('@entitiesRequest').then(({ response }) => {
          expect(response.statusCode).to.equal(200);
        });
        cy.url().should('match', especialidadePageUrlPattern);
      });

      it('last delete button click should delete instance of Especialidade', () => {
        cy.get(entityDeleteButtonSelector).last().click();
        cy.getEntityDeleteDialogHeading('especialidade').should('exist');
        cy.get(entityConfirmDeleteButtonSelector).click();
        cy.wait('@deleteEntityRequest').then(({ response }) => {
          expect(response.statusCode).to.equal(204);
        });
        cy.wait('@entitiesRequest').then(({ response }) => {
          expect(response.statusCode).to.equal(200);
        });
        cy.url().should('match', especialidadePageUrlPattern);

        especialidade = undefined;
      });
    });
  });

  describe('new Especialidade page', () => {
    beforeEach(() => {
      cy.visit(`${especialidadePageUrl}`);
      cy.get(entityCreateButtonSelector).click();
      cy.getEntityCreateUpdateHeading('Especialidade');
    });

    it('should create an instance of Especialidade', () => {
      cy.get(`[data-cy="idEspecialidade"]`).type('7207');
      cy.get(`[data-cy="idEspecialidade"]`).should('have.value', '7207');

      cy.get(`[data-cy="nomeEspecialidade"]`).type('dolores');
      cy.get(`[data-cy="nomeEspecialidade"]`).should('have.value', 'dolores');

      cy.get(entityCreateSaveButtonSelector).click();

      cy.wait('@postEntityRequest').then(({ response }) => {
        expect(response.statusCode).to.equal(201);
        especialidade = response.body;
      });
      cy.wait('@entitiesRequest').then(({ response }) => {
        expect(response.statusCode).to.equal(200);
      });
      cy.url().should('match', especialidadePageUrlPattern);
    });
  });
});
