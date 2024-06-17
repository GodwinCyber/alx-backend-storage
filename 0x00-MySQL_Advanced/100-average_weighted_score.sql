-- creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.
-- Procedure ComputeAverageScoreForUser is taking 1 input
-- user_id, a users.id value (you can assume user_id is linked to an existing users)
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE weighted_avg_score DECIMAL(10, 2);

    SELECT IFNULL(SUM(score * weight) / NULLIF(SUM(weight), 0), 0)
    INTO weighted_avg_score
    FROM scores
    WHERE user_id = user_id;

    UPDATE users
    SET average_score = weighted_avg_score
    WHERE id = user_id;
END$$

DELIMITER ;