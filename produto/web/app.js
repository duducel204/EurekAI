// EurekAI Web MVP Interactivity
document.addEventListener('DOMContentLoaded', () => {
    // State
    let currentTrack = 'curioso';
    let currentTopic = 'fotos';
    let currentAudience = '8anos';
    let currentTemp = 30;

    // Sandbox Response Matrix
    const responses = {
        fotos: {
            '8anos': {
                low: "A IA olha para milhares de fotos como se fossem quebra-cabeças. Ela aprendeu que se tiver duas orelhas pontudas, um focinho pequeno e bigodes, muito provavelmente é um gato!",
                med: "A IA funciona como um detetive de padrões. Ela compara os pontos da foto com uma grande 'galeria mental' que ela estudou. Se a combinação bater com o padrão de gato, ela diz 'É um gato!'",
                high: "A IA imagina um robô fotógrafo do futuro que examina os bigodes do gato e calcula que existe 99.8% de chance de ser um felino mágico galáctico!"
            },
            'curioso': {
                low: "A IA de visão computacional analisa pixels e formas geométicas na imagem. Ela compara esses dados numéricos com o padrão matemático que aprendeu ao analisar milhões de fotos de gatos.",
                med: "A IA extrai características (como o formato das orelhas e olhos) e calcula a probabilidade matemática da imagem corresponder ao conceito 'gato'.",
                high: "A IA combina o reconhecimento visual tradicional com descrições poéticas, sugerindo que a foto captura a essência graciosa e mistério felino."
            },
            'tecnico': {
                low: "Rede Neural Convolucional (CNN) processa a matriz de pixels extraindo mapas de características hierárquicas. A camada de saída Softmax retorna p(y=gato|X) ≈ 0.99.",
                med: "Arquitetura baseada em Vision Transformer (ViT) segmenta a imagem em patches de 16x16, aplicando mecanismos de auto-atenção para classificar o objeto principal.",
                high: "Modelo multimodal mapeia a imagem em um espaço latente compartilhado com embeddings de texto, correlacionando estatisticamente atributos visuais complexos."
            }
        },
        textos: {
            '8anos': {
                low: "A IA é como um jogo de completar palavras super rápido! Ela lê o que você escreveu e adivinha qual é a próxima palavra que faz mais sentido.",
                med: "Imagine um papagaio super inteligente que leu todos os livros do mundo. Quando você faz uma pergunta, ele junta as palavras que mais combinam juntas.",
                high: "A IA inventa uma historinha onde as palavras dançam em um carrossel e escolhem a palavra mais divertida para aparecer em seguida!"
            },
            'curioso': {
                low: "Modelos de linguagem analisam bilhões de textos para aprender quais palavras costumam vir depois de outras. Ela gera texto calculando a palavra mais provável.",
                med: "A IA não tem consciência ou sentimentos; ela calcula probabilidades matemáticas de sequências de palavras com base no contexto que você forneceu no prompt.",
                high: "A IA mistura o conhecimento factual com metáforas elaboradas, gerando um texto expressivo e ligeiramente imprevisível."
            },
            'tecnico': {
                low: "Decoder do Transformer utiliza atenção autorregressiva para prever o próximo token t_i amostrando da distribuição p(t_i | t_1...t_{i-1}).",
                med: "Através da arquitetura LLM com centenas de bilhões de parâmetros, o modelo ajusta o peso dos tensores via mecanismo de Multi-Head Attention.",
                high: "A amostragem de top-p/top-k com alta temperatura distorce a distribuição logit, aumentando a entropia na geração de respostas."
            }
        },
        erros: {
            '8anos': {
                low: "Como a IA não 'pensa' de verdade, às vezes ela tenta adivinhar uma palavra e erra feio! É por isso que sempre devemos conferir o que ela diz.",
                med: "Quando a IA não sabe a resposta exata, ela tenta inventar algo que soe parecido com a verdade para não ficar em silêncio.",
                high: "A IA dormiu no ponto, sonhou acordada e inventou que os dinossauros usavam óculos de sol na praia!"
            },
            'curioso': {
                low: "Isso se chama 'Alucinação'. A IA prioriza gerar um texto convincente sobre ser 100% verdadeira. Se faltarem dados, ela preenche as lacunas com estimativas plausíveis.",
                med: "A IA calcula a coerência gramatical do texto, não a veracidade factual dos fatos. Por isso ela pode escrever uma mentira com tom de total certeza.",
                high: "Quando a temperatura/criatividade está alta, a IA combina fatos reais com dados totalmente fictícios de forma indistinguível."
            },
            'tecnico': {
                low: "Alucinações ocorrem devido a falhas no alinhamento do dataset de treino, onde a otimização da função de perda prioriza a perplexidade do modelo sobre a fidelidade dos fatos.",
                med: "A ausência de mecanismo de RAG (Retrieval-Augmented Generation) força o modelo a confiar unicamente nos pesos estáticos do pré-treino.",
                high: "Vetos de atenção em camadas profundas ativam nós de alta variação sem grounding conceitual, gerando outputs de baixa precisão."
            }
        }
    };

    // Hallucination Game Questions
    const gameQuestions = [
        {
            topic: "História e Ciência da Computação",
            options: [
                { text: "Ada Lovelace é considerada a primeira programadora da história por seu trabalho no motor analítico.", correct: false },
                { text: "O ENIAC foi um dos primeiros computadores digitais de propósito geral.", correct: false },
                { text: "Albert Einstein inventou o primeiro microprocessador intel 8080 em 1955 enquanto trabalhava na Suíça.", correct: true, explanation: "🚨 ALUCINAÇÃO DETECTADA! Einstein faleceu em 1955 e era físico teórico. O microprocessador Intel 8080 foi criado em 1974 por Federico Faggin e Marcian Hoff." }
            ]
        }
    ];

    // DOM Elements
    const trackCards = document.querySelectorAll('.track-card');
    const topicSelect = document.getElementById('topic-select');
    const audienceBtns = document.querySelectorAll('#audience-group .pill-btn');
    const tempSlider = document.getElementById('temp-slider');
    const tempDisplay = document.getElementById('temp-value-display');
    const sandboxResult = document.getElementById('sandbox-result');
    const evidenceTrigger = document.getElementById('evidence-trigger');
    const principleBox = document.getElementById('principle-box');
    const gameOptionsContainer = document.getElementById('game-options');
    const gameFeedback = document.getElementById('game-feedback');

    // Update Sandbox UI
    function updateSandbox() {
        let tempCategory = 'med';
        if (currentTemp < 25) tempCategory = 'low';
        else if (currentTemp > 70) tempCategory = 'high';

        // Update Slider Text
        if (currentTemp < 25) tempDisplay.textContent = `${currentTemp}% (Factual / Rigoroso)`;
        else if (currentTemp > 70) tempDisplay.textContent = `${currentTemp}% (Alta Criatividade / Risco de Erro)`;
        else tempDisplay.textContent = `${currentTemp}% (Equilibrado)`;

        // Fetch Response
        const topicData = responses[currentTopic] || responses['fotos'];
        const audienceData = topicData[currentAudience] || topicData['curioso'];
        const text = audienceData[tempCategory] || "Resposta simulada.";

        sandboxResult.innerHTML = `<p>${text}</p>`;
    }

    // Event Listeners for Sandbox
    trackCards.forEach(card => {
        card.addEventListener('click', () => {
            trackCards.forEach(c => c.classList.remove('active'));
            card.classList.add('active');
            currentTrack = card.dataset.track;
        });
    });

    topicSelect.addEventListener('change', (e) => {
        currentTopic = e.target.value;
        updateSandbox();
    });

    audienceBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            audienceBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentAudience = btn.dataset.audience;
            updateSandbox();
        });
    });

    tempSlider.addEventListener('input', (e) => {
        currentTemp = parseInt(e.target.value);
        updateSandbox();
    });

    evidenceTrigger.addEventListener('click', () => {
        principleBox.classList.toggle('hidden');
    });

    // Render Hallucination Game
    function renderGame() {
        const question = gameQuestions[0];
        gameOptionsContainer.innerHTML = '';
        gameFeedback.classList.add('hidden');

        question.options.forEach((opt, idx) => {
            const btn = document.createElement('button');
            btn.className = 'game-option-card';
            btn.textContent = `${idx + 1}. ${opt.text}`;
            btn.addEventListener('click', () => handleGameChoice(opt, btn));
            gameOptionsContainer.appendChild(btn);
        });
    }

    function handleGameChoice(option, btnElement) {
        const allOptionBtns = gameOptionsContainer.querySelectorAll('.game-option-card');
        allOptionBtns.forEach(b => b.disabled = true);

        gameFeedback.classList.remove('hidden', 'correct-feedback', 'incorrect-feedback');

        if (option.correct) {
            btnElement.classList.add('correct');
            gameFeedback.classList.add('correct-feedback');
            gameFeedback.innerHTML = `<strong>🎯 Parabéns! Você encontrou a alucinação!</strong><br>${option.explanation}`;
        } else {
            btnElement.classList.add('incorrect');
            gameFeedback.classList.add('incorrect-feedback');
            gameFeedback.innerHTML = `<strong>❌ Essa afirmação é verdadeira!</strong><br>Procure a afirmação que contém um fato histórico ou científico inventado pela IA.`;
        }
    }

    // Init
    updateSandbox();
    renderGame();
});
