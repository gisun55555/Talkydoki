-- Enum 값 추가
ALTER TABLE `ai_chat_room`
    MODIFY COLUMN `category` ENUM('HOTEL_CHECK_IN', 'CHANGE_AT_CONVENIENCE_STORE','SOCCER_CONVERSATION','ORDER_HAMBURGER','HAIRCUT_AT_SALON','DESCRIBE_HEALTH_CONDITION_AT_HOSPITAL','FIND_LOST_ITEM_AT_POLICE_STATION','ENGAGE_IN_SOCIAL_DISCUSSION','BEFRIEND_A_COLLEAGUE','BRUNCH_CONVERSATION') NOT NULL;
