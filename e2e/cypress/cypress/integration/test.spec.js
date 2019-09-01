describe('My First Test', function() {
  it('clicks the moving button', function() {
    cy.visit('http://localhost:8080')

    cy.get('#button1').click({force: true})
  })
})
