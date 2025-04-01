document.addEventListener("DOMContentLoaded", loadTasks);

function addTask() {
    let taskInput = document.getElementById("task");
    let taskValue = taskInput.value.trim();
    
    if (taskValue === "") return;

    let taskList = document.getElementById("task-list");

    let li = document.createElement("li");
    li.textContent = taskValue;
    li.onclick = toggleTask;
    
    let deleteBtn = document.createElement("button");
    deleteBtn.textContent = "X";
    deleteBtn.onclick = deleteTask;

    li.appendChild(deleteBtn);
    taskList.appendChild(li);
    
    saveTasks();
    taskInput.value = "";
}

function toggleTask(event) {
    event.target.classList.toggle("completed");
    saveTasks();
}

function deleteTask(event) {
    event.stopPropagation();
    event.target.parentElement.remove();
    saveTasks();
}

function saveTasks() {
    let tasks = [];
    document.querySelectorAll("#task-list li").forEach(li => {
        tasks.push({
            text: li.firstChild.textContent,
            completed: li.classList.contains("completed")
        });
    });
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

function loadTasks() {
    let savedTasks = JSON.parse(localStorage.getItem("tasks")) || [];
    let taskList = document.getElementById("task-list");

    savedTasks.forEach(task => {
        let li = document.createElement("li");
        li.textContent = task.text;
        if (task.completed) li.classList.add("completed");
        li.onclick = toggleTask;

        let deleteBtn = document.createElement("button");
        deleteBtn.textContent = "X";
        deleteBtn.onclick = deleteTask;

        li.appendChild(deleteBtn);
        taskList.appendChild(li);
    });
}
