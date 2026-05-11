/**
 * App.js — Todo List (View Layer)
 *
 * Gerencia a interação com a API REST, renderização dinâmica
 * dos cards de tarefas, filtros, calendário e saudação.
 */

// ============================================================
// CONSTANTS & STATE
// ============================================================

const API_URL = '/api/tasks';

const state = {
    tasks: [],
    currentFilter: 'all',
    searchQuery: '',
    calendarDate: new Date(),
    countDone: 0,
    countPending: 0,
    editingTaskId: null,
};

// ============================================================
// DOM REFERENCES
// ============================================================

const $ = (sel) => document.querySelector(sel);
const $$ = (sel) => document.querySelectorAll(sel);

const dom = {
    form:       $('#add-task-form'),
    titleInput: $('#task-title'),
    descInput:  $('#task-desc'),
    taskGrid:   $('#task-grid'),
    statDone:   $('#stat-done'),
    statPending:$('#stat-pending'),
    greeting:   $('#greeting'),
    sidebarDay: $('#sidebar-day'),
    sidebarDate:$('#sidebar-date'),
    calTitle:   $('#calendar-title'),
    calGrid:    $('#calendar-grid'),
    calPrev:    $('#cal-prev'),
    calNext:    $('#cal-next'),
    filters:    $('#filters'),
    searchInput:$('#search-input'),
    toasts:     $('#toast-container'),
    editModal:  $('#edit-modal'),
    editForm:   $('#edit-form'),
    editTitleInput: $('#edit-task-title'),
    editDescInput: $('#edit-task-desc'),
    editCancelBtn: $('#edit-cancel-btn'),
};

// ============================================================
// API LAYER
// ============================================================

async function fetchTasks(filter = 'all') {
    try {
        const res = await fetch(`${API_URL}?filter=${filter}`);
        const data = await res.json();
        return data;
    } catch (err) {
        showToast('Erro ao carregar tarefas.', 'error');
        return { tasks: [], count_done: 0, count_pending: 0 };
    }
}

async function createTask(title, description) {
    try {
        const res = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title, description }),
        });
        if (!res.ok) {
            const err = await res.json();
            showToast(err.error || 'Erro ao criar tarefa.', 'error');
            return null;
        }
        return await res.json();
    } catch (err) {
        showToast('Erro de conexão.', 'error');
        return null;
    }
}

async function deleteTask(id) {
    try {
        const res = await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
        return res.ok;
    } catch {
        showToast('Erro ao remover tarefa.', 'error');
        return false;
    }
}

async function toggleTask(id) {
    try {
        const res = await fetch(`${API_URL}/${id}/toggle`, { method: 'PATCH' });
        if (!res.ok) return null;
        return await res.json();
    } catch {
        showToast('Erro ao atualizar tarefa.', 'error');
        return null;
    }
}

async function editTask(id, title, description) {
    try {
        const res = await fetch(`${API_URL}/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title, description }),
        });
        if (!res.ok) {
            const err = await res.json();
            showToast(err.error || 'Erro ao editar tarefa.', 'error');
            return null;
        }
        return await res.json();
    } catch (err) {
        showToast('Erro de conexão.', 'error');
        return null;
    }
}

// ============================================================
// RENDERING
// ============================================================

function renderTasks() {
    let filtered = state.tasks;

    // Client-side search filter
    if (state.searchQuery) {
        const q = state.searchQuery.toLowerCase();
        filtered = filtered.filter(t =>
            t.title.toLowerCase().includes(q) ||
            (t.description && t.description.toLowerCase().includes(q))
        );
    }

    if (filtered.length === 0) {
        dom.taskGrid.className = 'task-grid task-grid--empty';
        dom.taskGrid.innerHTML = `
            <div class="task-grid__empty-icon"><i data-lucide="clipboard-list"></i></div>
            <div class="task-grid__empty-text">Nenhuma tarefa encontrada</div>
            <div class="task-grid__empty-hint">Adicione sua primeira tarefa acima!</div>
        `;
        lucide.createIcons();
        return;
    }

    dom.taskGrid.className = 'task-grid';
    dom.taskGrid.innerHTML = filtered.map((task, i) => `
        <div class="task-card ${task.done ? 'task-card--done' : ''}"
             data-id="${task.id}"
             style="animation-delay: ${i * 0.05}s">
            <input
                type="checkbox"
                class="task-card__check"
                id="check-${task.id}"
                ${task.done ? 'checked' : ''}
                aria-label="Marcar tarefa como ${task.done ? 'pendente' : 'concluída'}"
            >
            <div class="task-card__content">
                <div class="task-card__title">${escapeHtml(task.title)}</div>
                ${task.description ? `<div class="task-card__desc">${escapeHtml(task.description)}</div>` : ''}
                <div class="task-card__meta">
                    <i data-lucide="calendar" class="task-card__meta-icon"></i>
                    <span>${formatDate(task.created_at)}</span>
                </div>
            </div>
            <div class="task-card__actions">
                <button
                    class="task-card__action-btn task-card__action-btn--edit"
                    data-edit="${task.id}"
                    aria-label="Editar tarefa"
                    title="Editar">
                    <i data-lucide="edit-2"></i>
                </button>
                <button
                    class="task-card__action-btn task-card__action-btn--delete"
                    data-delete="${task.id}"
                    aria-label="Excluir tarefa"
                    title="Excluir">
                    <i data-lucide="trash-2"></i>
                </button>
            </div>
        </div>
    `).join('');

    lucide.createIcons();
}

function renderStats() {
    dom.statDone.textContent = String(state.countDone).padStart(2, '0');
    dom.statPending.textContent = String(state.countPending).padStart(2, '0');
}

// ============================================================
// CALENDAR
// ============================================================

function renderCalendar() {
    const date = state.calendarDate;
    const year = date.getFullYear();
    const month = date.getMonth();

    const monthNames = [
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro',
    ];

    dom.calTitle.textContent = `${monthNames[month]} ${year}`;

    // Weekday headers
    const weekdays = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'];
    let html = weekdays.map((d, i) =>
        `<span class="calendar__weekday ${i >= 5 ? 'calendar__weekday--weekend' : ''}">${d}</span>`
    ).join('');

    // First day of month (adjust for Monday start)
    const firstDay = new Date(year, month, 1);
    let startWeekday = firstDay.getDay() - 1; // Monday = 0
    if (startWeekday < 0) startWeekday = 6;

    const daysInMonth = new Date(year, month + 1, 0).getDate();
    const daysInPrevMonth = new Date(year, month, 0).getDate();

    const today = new Date();
    const isCurrentMonth = today.getFullYear() === year && today.getMonth() === month;

    // Previous month days
    for (let i = startWeekday - 1; i >= 0; i--) {
        const day = daysInPrevMonth - i;
        html += `<button class="calendar__day calendar__day--other-month" tabindex="-1">${day}</button>`;
    }

    // Current month days
    for (let d = 1; d <= daysInMonth; d++) {
        const isToday = isCurrentMonth && d === today.getDate();
        const dayOfWeek = (startWeekday + d - 1) % 7;
        const isWeekend = dayOfWeek >= 5;
        const classes = [
            'calendar__day',
            isToday ? 'calendar__day--today' : '',
            isWeekend && !isToday ? 'calendar__day--weekend' : '',
        ].filter(Boolean).join(' ');
        html += `<button class="${classes}">${d}</button>`;
    }

    // Next month days (fill remaining)
    const totalCells = startWeekday + daysInMonth;
    const remaining = totalCells % 7 === 0 ? 0 : 7 - (totalCells % 7);
    for (let d = 1; d <= remaining; d++) {
        html += `<button class="calendar__day calendar__day--other-month" tabindex="-1">${d}</button>`;
    }

    dom.calGrid.innerHTML = html;
}

// ============================================================
// GREETING & DATE
// ============================================================

function updateGreeting() {
    const hour = new Date().getHours();
    let greeting;
    if (hour < 12) greeting = 'Bom dia';
    else if (hour < 18) greeting = 'Boa tarde';
    else greeting = 'Boa noite';

    dom.greeting.innerHTML = `${greeting}, <strong>Allicia</strong> <span>, comece a planejar hoje</span>`;
}

function updateSidebarDate() {
    const now = new Date();
    const dayNames = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'];

    dom.sidebarDay.textContent = dayNames[now.getDay()];

    const options = { day: '2-digit', month: 'long', year: 'numeric' };
    dom.sidebarDate.textContent = now.toLocaleDateString('pt-BR', options);
}

// ============================================================
// TOAST NOTIFICATIONS
// ============================================================

function showToast(message, type = 'success') {
    const toast = document.createElement('div');
    toast.className = `toast toast--${type}`;
    toast.textContent = message;
    dom.toasts.appendChild(toast);

    setTimeout(() => {
        toast.classList.add('toast--removing');
        setTimeout(() => toast.remove(), 400);
    }, 3000);
}

// ============================================================
// UTILITIES
// ============================================================

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function formatDate(isoString) {
    if (!isoString) return '';
    try {
        const date = new Date(isoString);
        return date.toLocaleDateString('pt-BR', {
            day: '2-digit',
            month: '2-digit',
            year: 'numeric',
            hour: '2-digit',
            minute: '2-digit',
        });
    } catch {
        return isoString;
    }
}

// ============================================================
// DATA LOADING
// ============================================================

async function loadTasks() {
    const data = await fetchTasks(state.currentFilter);
    state.tasks = data.tasks || [];
    state.countDone = data.count_done || 0;
    state.countPending = data.count_pending || 0;
    renderTasks();
    renderStats();
}

// ============================================================
// EVENT HANDLERS
// ============================================================

function setupEventListeners() {
    // Add task
    dom.form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const title = dom.titleInput.value.trim();
        const desc = dom.descInput.value.trim();
        if (!title) return;

        const task = await createTask(title, desc);
        if (task) {
            dom.titleInput.value = '';
            dom.descInput.value = '';
            dom.titleInput.focus();
            showToast('Tarefa adicionada!');
            await loadTasks();
        }
    });

    // Task grid delegation: checkbox & delete
    dom.taskGrid.addEventListener('click', async (e) => {
        const checkbox = e.target.closest('.task-card__check');
        if (checkbox) {
            const card = checkbox.closest('.task-card');
            const id = parseInt(card.dataset.id);
            await toggleTask(id);
            await loadTasks();
            return;
        }

        const deleteBtn = e.target.closest('[data-delete]');
        if (deleteBtn) {
            const id = parseInt(deleteBtn.dataset.delete);
            const card = deleteBtn.closest('.task-card');
            card.classList.add('task-card--removing');
            setTimeout(async () => {
                const ok = await deleteTask(id);
                if (ok) {
                    showToast('Tarefa removida.');
                }
                await loadTasks();
            }, 350);
            return;
        }

        const editBtn = e.target.closest('[data-edit]');
        if (editBtn) {
            const id = parseInt(editBtn.dataset.edit);
            const task = state.tasks.find(t => t.id === id);
            if (task) {
                state.editingTaskId = id;
                dom.editTitleInput.value = task.title;
                dom.editDescInput.value = task.description || '';
                dom.editModal.classList.add('modal-overlay--active');
                dom.editTitleInput.focus();
            }
            return;
        }
    });

    // Edit Modal Events
    dom.editCancelBtn.addEventListener('click', () => {
        dom.editModal.classList.remove('modal-overlay--active');
        state.editingTaskId = null;
    });

    dom.editForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        if (!state.editingTaskId) return;

        const title = dom.editTitleInput.value.trim();
        const desc = dom.editDescInput.value.trim();
        if (!title) return;

        const task = await editTask(state.editingTaskId, title, desc);
        if (task) {
            dom.editModal.classList.remove('modal-overlay--active');
            state.editingTaskId = null;
            showToast('Tarefa atualizada!');
            await loadTasks();
        }
    });

    // Filters
    dom.filters.addEventListener('click', async (e) => {
        const pill = e.target.closest('.filters__pill');
        if (!pill) return;

        $$('.filters__pill').forEach(p => p.classList.remove('filters__pill--active'));
        pill.classList.add('filters__pill--active');

        state.currentFilter = pill.dataset.filter;
        await loadTasks();
    });

    // Search
    dom.searchInput.addEventListener('input', () => {
        state.searchQuery = dom.searchInput.value.trim();
        renderTasks();
    });

    // Calendar navigation
    dom.calPrev.addEventListener('click', () => {
        state.calendarDate.setMonth(state.calendarDate.getMonth() - 1);
        renderCalendar();
    });

    dom.calNext.addEventListener('click', () => {
        state.calendarDate.setMonth(state.calendarDate.getMonth() + 1);
        renderCalendar();
    });

    // Keyboard shortcut: Enter to add task
    dom.descInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            e.preventDefault();
            dom.form.dispatchEvent(new Event('submit'));
        }
    });
}

// ============================================================
// INITIALIZATION
// ============================================================

document.addEventListener('DOMContentLoaded', () => {
    updateGreeting();
    updateSidebarDate();
    renderCalendar();
    setupEventListeners();
    loadTasks();

    // Initialize Lucide icons in static HTML
    lucide.createIcons();

    // Auto-refresh greeting every minute
    setInterval(updateGreeting, 60_000);
});
