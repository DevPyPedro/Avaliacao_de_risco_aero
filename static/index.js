let currentStep = 1;

function nextStep() {
    document.getElementById(`div${currentStep}`).classList.remove('active');
    currentStep++;
    document.getElementById(`div${currentStep}`).classList.add('active');
}

function prevStep() {
    document.getElementById(`div${currentStep}`).classList.remove('active');
    currentStep--;
    document.getElementById(`div${currentStep}`).classList.add('active');
}

function showResults() {

    let results = {};
    
    let fields = ['modelo', 'categoria', 'comprimento', 'envergadura', 'altura', 'raio_curva', 'distancia_tremPouso_pavimenato', 'distancia_tremPouso_taxi', 'codigo', 'largura_pista', 'largura_pista_taxi', 'largura_faixa', 'acostamento', 'desvio_lateral', 'mtow', 'margem_seguranca'];

    for (let i = 0; i < fields.length; i++) {
        let value = document.getElementById(fields[i]).value;
        results[fields[i]] = value;
    }

    fetch('/save', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(results)
    }).then(response => {
        if (response.ok) {
            console.log('Dados salvos com sucesso!');
        } else {
            console.error('Erro ao salvar dados');
        }
    });
}

