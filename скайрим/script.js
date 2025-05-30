document.addEventListener('DOMContentLoaded', () => {
    const menuButton = document.getElementById('menu-toggle');
    const effectsMenu = document.getElementById('effects-menu');
    const mainTable = document.getElementById('main-table').querySelector('tbody');
    const selectionTable = document.getElementById('selection-table').querySelector('tbody');
    const backButton = document.getElementById('back-btn');

    let data = [];
    let effects = [];
    let positiveNegativeData = {};

    // Загрузка данных из JSON файлов
    async function loadData() {
        try {
            const dataResponse = await fetch('data.json');
            const effectsResponse = await fetch('effects.json');
            const positiveNegativeResponse = await fetch('positive_negative_data.json');
            
            // Обработка всех данных
            data = await dataResponse.json();
            effects = await effectsResponse.json();
            positiveNegativeData = await positiveNegativeResponse.json();

            loadTableData(data);
            loadEffectMenu();
        } catch (error) {
            console.error('Ошибка при загрузке данных:', error);
        }
    }

    // Функция для загрузки данных в таблицу
    function loadTableData(data) {
        mainTable.innerHTML = '';

        // Сортировка: сначала положительные и смешанные эффекты, потом отрицательные
        data.sort((a, b) => {
            const aNegative = a.effects.every(effect => positiveNegativeData.negative_effects.includes(effect));
            const bNegative = b.effects.every(effect => positiveNegativeData.negative_effects.includes(effect));

            if (aNegative && !bNegative) return 1;
            if (!aNegative && bNegative) return -1;

            return a.name.localeCompare(b.name); // Сортировка по имени, если эффекты одинаковы
        });

        data.forEach(item => {
            const row = document.createElement('tr');
            const nameCell = document.createElement('td');
            nameCell.textContent = item.name;
            row.appendChild(nameCell);

            let isMixed = false;
            let isPositive = true;

            item.effects.forEach(effect => {
                const effectCell = document.createElement('td');
                effectCell.textContent = effect;

                if (positiveNegativeData.positive_effects.includes(effect)) {
                    effectCell.classList.add('green-bg');
                } else if (positiveNegativeData.negative_effects.includes(effect)) {
                    effectCell.classList.add('red-bg');
                    isPositive = false;
                } else {
                    isMixed = true;
                }

                row.appendChild(effectCell);
            });

            // Определяем фон для ячейки с названием в зависимости от эффектов
            if (isPositive && !isMixed) {
                row.classList.add('green-bg');
            } else if (isMixed) {
                row.classList.add('mixed-bg');
            } else {
                row.classList.add('red-bg');
            }

            mainTable.appendChild(row);
        });
    }

    // Загрузка эффектов в меню
    function loadEffectMenu() {
        effectsMenu.innerHTML = '';  // очищаем меню

        effects.forEach(effect => {
            const button = document.createElement('button');
            button.textContent = effect.effect;
            button.addEventListener('click', () => filterByEffect(effect.effect));
            effectsMenu.appendChild(button);
        });
    }

    // Фильтрация данных по выбранному эффекту
    function filterByEffect(effectName) {
        selectionTable.innerHTML = '';
        const filteredData = data.filter(item => item.effects.includes(effectName));
        filteredData.forEach(item => {
            const row = document.createElement('tr');
            const nameCell = document.createElement('td');
            nameCell.textContent = item.name;
            row.appendChild(nameCell);

            item.effects.forEach(effect => {
                const effectCell = document.createElement('td');
                effectCell.textContent = effect;
                row.appendChild(effectCell);
            });

            selectionTable.appendChild(row);
        });

        document.getElementById('main-table').classList.add('hidden');
        document.getElementById('selection-table').classList.remove('hidden');
    }

    // Обработчик нажатия на кнопку меню
    menuButton.addEventListener('click', () => {
        effectsMenu.style.display = effectsMenu.style.display === 'none' ? 'block' : 'none';
    });

    // Обработчик кнопки назад
    backButton.addEventListener('click', () => {
        document.getElementById('selection-table').classList.add('hidden');
        document.getElementById('main-table').classList.remove('hidden');
    });

    // Инициализация загрузки данных
    loadData();
});
