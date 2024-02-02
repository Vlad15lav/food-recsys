from database.queries import add_user


def start_handler(bot, message, db):
    """
    Логика обработки команды /start
    Отправка приветственного сообщения пользователю
    """
    add_user(db, message.from_user.id)
    bot.send_message(message.chat.id,
                     "Привет! Я – AI Chef бот. С моей помощью вы можете " +
                     "удобнее и быстрее подобрать для себя рецепт блюда. " +
                     "Присылайте ваши пожелания, а я порекомендую " +
                     "подходящий рецепт. Примеры запросов: " +
                     "«Предложи что-нибудь из помидоров, " +
                     "лука и курицы» или «Десерт из шоколада и фруктов»." +
                     "Пожалуйста, не забывайте оставлять " +
                     "оценки после моих рекомендаций. " +
                     "Оценки помогают мне становиться лучше и точнее.")