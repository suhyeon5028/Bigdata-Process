package site.metacoding.mongocrud.domain;

import java.time.LocalDateTime;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@AllArgsConstructor
@NoArgsConstructor
@Data
@Document(collection = "navers")
public class Naver {
    @Id
    private String _id;
    private String company;
    private String title;
    private LocalDateTime createdAt;

    public LocalDateTime getCreatedAt(){
        return createdAt.minusHours(9);
    }
}
