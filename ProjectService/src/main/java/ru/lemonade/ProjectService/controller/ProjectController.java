package ru.lemonade.ProjectService.controller;

import lombok.AllArgsConstructor;
import lombok.NonNull;
import ru.lemonade.ProjectService.model.Project;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import ru.lemonade.ProjectService.service.ProjectService;

import java.util.List;

@RestController
@RequestMapping("api/v1/projects")
@AllArgsConstructor
public class ProjectController {
    @NonNull
    private final ProjectService projectService;

    @GetMapping
    public List<Project> getProjects() {
        return List.of();
    }
}
