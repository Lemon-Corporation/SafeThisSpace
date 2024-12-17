package ru.lemonade.ProjectService.service.impl;

import lombok.AllArgsConstructor;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Service;
import ru.lemonade.ProjectService.model.Project;
import ru.lemonade.ProjectService.repository.ProjectRepository;
import ru.lemonade.ProjectService.service.ProjectService;

import java.util.List;

@Service
@Primary
@AllArgsConstructor
public class ProjectServiceImpl implements ProjectService {
    private ProjectRepository projectRepository;


    @Override
    public List<Project> getProjects() {
        return projectRepository.findAll();
    }

    @Override
    public Project getProject(int id) {
        return projectRepository.getReferenceById((long) id);
    }

    @Override
    public Project getProject(Long id) {
        return projectRepository.getReferenceById(id);
    }

    @Override
    public Project addProject(Project project) {
        return projectRepository.save(project);
    }

    @Override
    public Project updateProject(Project project) {
        return projectRepository.save(project);
    }

    @Override
    public void deleteProject(Long id) {
        projectRepository.deleteById(id);
    }

    @Override
    public void deleteProject(int id) {
        projectRepository.deleteById((long)id);
    }

    @Override
    public Project getProjectByLink(String link) {
        return projectRepository.findByRepoUrl(link).orElse(null);
    }

    @Override
    public Project getProjectByName(String name) {
        return projectRepository.findByName(name).orElse(null);
    }
}
