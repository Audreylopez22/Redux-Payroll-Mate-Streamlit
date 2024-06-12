
describe('Login Test', () => {
  it('should login and go to load_sheet page', () => {
    cy.visit('/Login');

    cy.get('input[aria-label="Username"]').type('audrey')
    cy.get('input[aria-label="Password"]').type('88888888')

    cy.get('[data-testid="baseButton-secondaryFormSubmit"]').should('be.visible').click().click()
    cy.wait(2000)
    cy.contains('Welcome').should('exist')

    cy.get('a[href="http://streamlit_redux_PM:8501/Load_Sheet"]').click()

    cy.fixture('test.xlsx', 'binary').then(fileContent => {
      cy.get('input[type="file"]').attachFile('test.xlsx')

      cy.contains('Making modifications to the Excel file...').should('exist')
      cy.contains('Saving modifications to the Excel file...').should('exist')
      cy.contains('Download modified file').should('exist').click()
    });
  });
});
