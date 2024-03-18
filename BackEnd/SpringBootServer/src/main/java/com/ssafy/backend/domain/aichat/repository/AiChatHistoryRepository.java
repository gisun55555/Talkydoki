package com.ssafy.backend.domain.aichat.repository;

import com.ssafy.backend.domain.aichat.entity.AiChat;
import com.ssafy.backend.domain.aichat.entity.AiChatHistory;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface AiChatHistoryRepository extends JpaRepository<AiChatHistory,Long> {
    List<AiChat> findByAiChatRoomId(Long roomId);
}
