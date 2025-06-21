const mathsteps = require('mathsteps');

// Pega a equação passada como argumento
const args = process.argv.slice(2);

if (args.length === 0) {
    console.error("Erro: você deve passar uma equação como argumento.");
    console.error("Exemplo: node script.js '2x + 3x = 5'");
    process.exit(1);
}

const inputEquation = args[0];

// Resolve a equação
const steps = mathsteps.solveEquation(inputEquation);

// Exibe os passos
steps.forEach(step => {
    console.log("before change: " + step.oldEquation.ascii());
    console.log("change: " + step.changeType);
    console.log("after change: " + step.newEquation.ascii());
    console.log("# of substeps: " + step.substeps.length);
});
