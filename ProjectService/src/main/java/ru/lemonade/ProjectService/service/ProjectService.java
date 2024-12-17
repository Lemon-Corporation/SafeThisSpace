package ru.lemonade.ProjectService.service;

import ru.lemonade.ProjectService.model.Project;

import java.util.List;

public interface ProjectService {
    List<Project> getProjects();
    Project getProject(int id);

    Project getProject(Long id);

    Project addProject(Project project);
    Project updateProject(Project project);
    void deleteProject(Long id);
    void deleteProject(int id);
    Project getProjectByLink(String link);
    Project getProjectByName(String name);
}
