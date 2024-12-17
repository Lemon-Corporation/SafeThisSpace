package ru.lemonade.ProjectService.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import ru.lemonade.ProjectService.model.Project;

import java.util.Optional;

@Repository
public interface ProjectRepository extends JpaRepository<Project, Long> {
    Optional<Project> findByRepoUrl(String repoUrl);
    Optional<Project> findByName(String name);
}