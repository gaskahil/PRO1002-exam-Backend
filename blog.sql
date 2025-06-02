CREATE TABLE posts (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    date TEXT NOT NULL,
    excerpt TEXT NOT NULL,
    body TEXT NOT NULL,
);

INSERT INTO posts (id, title, date, excerpt, body) VALUES (
    1,
    'The Power of Morning Routines',
    '2025-06-02',
    'Starting your day with a consistent morning routine can boost productivity, reduce stress, and improve focus.',
    'Starting your day with a consistent morning routine can boost productivity, 
reduce stress, and improve focus. Whether it''s a quick workout, journaling, 
or mindful meditation, taking 30 minutes each morning for yourself sets 
the tone for the rest of the day. It''s not about perfection—it''s about intention.'
);

INSERT INTO posts (id, title, date, excerpt, body) VALUES (
    2,
    'Exploring the Wonders of Space',
    '2025-06-05',
    'Space exploration continues to unveil the mysteries of the universe, from black holes to distant galaxies.',
    'Space exploration continues to unveil the mysteries of the universe,
from black holes to distant galaxies. With advancements in technology,
we are now able to send probes to the farthest reaches of our solar system,
and even beyond. The discoveries made by missions like the Hubble Space Telescope
and the Mars rovers have expanded our understanding of the cosmos and our place within it.'
);

INSERT INTO posts (id, title, date, excerpt, body) VALUES (
    3,
    'The Art of Minimalist Living',
    '2025-06-08',
    'Embracing minimalism can lead to a more fulfilling life by reducing clutter and focusing on what truly matters.',
    'Embracing minimalism can lead to a more fulfilling life by focusing on what truly matters.
Minimalism is not just about decluttering your physical space, but also about simplifying your mental and emotional load.
By letting go of excess, you can create room for experiences and relationships that bring joy and meaning to your life. 
It''s about quality over quantity, and finding beauty in simplicity.'
);

INSERT INTO posts (id, title, date, excerpt, body) VALUES (
    4,
    'The Future of Renewable Energy',
    '2025-06-11',
    'Renewable energy sources are crucial for a sustainable future, reducing our reliance on fossil fuels.',
    'Renewable energy sources like solar, wind, and hydroelectric power are crucial for a sustainable future.
By reducing our reliance on fossil fuels, we can mitigate climate change and protect our planet for future generations.
Investing in renewable energy technologies not only helps the environment but also creates jobs and stimulates economic growth.
As we continue to innovate and improve energy efficiency, the transition to a greener economy becomes more achievable.'
);

INSERT INTO posts (id, title, date, excerpt, body) VALUES (
    5,
    'The power of a good cup of coffee',
    '2025-05-20',
    'A good cup of coffee can transform your morning, energizing you for the day ahead.',
    'A good cup of coffee can transform your morning, energizing you for the day ahead.
From the rich aroma to the first sip, coffee is more than just a beverage; it''s a ritual for many.
Whether you prefer a dark roast or a light blend, the right coffee can awaken your senses and set a positive tone for the day.
It''s not just about caffeine; it''s about the experience, the warmth, and the comfort that a good cup of coffee brings.'
);

INSERT INTO posts (id, title, date, excerpt, body) VALUES (
    6,
    'Solar Power: Harnessing the Sun''s Energy',
    '2025-05-25',
    'Solar power is a clean and renewable energy source that can significantly reduce our carbon footprint.',
    'Solar power is a clean and renewable energy source that can significantly reduce our carbon footprint.
By converting sunlight into electricity, solar panels provide a sustainable solution to our energy needs.
As technology advances, solar energy becomes more efficient and affordable, making it accessible to more people.
The transition to solar power not only helps combat climate change but also promotes energy independence and security.
It''s a step towards a greener future, where we can harness the sun''s energy to power our homes and businesses.'
);

INSERT INTO posts (id, title, date, excerpt, body) VALUES (
    7,
    'The Benefits of Daily Exercise',
    '2025-06-20',
    'Incorporating daily exercise into your routine can lead to improved physical and mental health.',
    'Incorporating daily exercise into your routine can lead to improved physical and mental health.
Exercise releases endorphins, which can boost your mood and reduce stress.
Whether it''s a brisk walk, a gym session, or yoga, finding an activity you enjoy makes it easier to stick with it.
Regular physical activity not only helps maintain a healthy weight but also strengthens your heart, muscles, and bones.
It''s a holistic approach to wellness that benefits both body and mind.'
);

INSERT INTO posts (id, title, date, excerpt, body) VALUES (
    8,
    'The Vast Space of the Universe',
    '2025-06-30',
    'The universe is a vast and mysterious place, filled with wonders waiting to be explored.',
    'The universe is a vast and mysterious place, filled with wonders waiting to be explored.
From the smallest particles to the largest galaxies, the cosmos offers endless opportunities for discovery.
With advancements in technology, we can now observe distant stars, planets, and even black holes.
The study of space not only satisfies our curiosity but also helps us understand the fundamental laws of physics and the origins of our universe.
As we continue to explore the cosmos, we uncover the secrets of our existence and our place in the universe.'
);

INSERT INTO posts (id, title, date, excerpt, body) VALUES (
    9,
    'The Art of Cooking at Home',
    '2025-07-05',
    'Cooking is not just a necessity; it''s an art that brings people together and creates lasting memories.',
    'Cooking is not just a necessity; it''s an art that brings people together and creates lasting memories.
From experimenting with new recipes to sharing meals with loved ones, cooking is a creative outlet that nourishes both body and soul.
Whether you''re a seasoned chef or a beginner, the kitchen is a place where you can express yourself and explore different cultures through food.
Cooking allows us to connect with others, share traditions, and create experiences that linger long after the meal is over.
It''s a celebration of flavors, textures, and aromas that can transform an ordinary day into something special.'
);

INSERT INTO posts (id, title, date, excerpt, body) VALUES (
    10,
    'The Journey of Self-Discovery',
    '2025-07-10',
    'Self-discovery is a lifelong journey that helps us understand our true selves and our place in the world.',
    'Self-discovery is a lifelong journey that helps us understand our true selves and our place in the world.
It''s about exploring our passions, values, and beliefs, and learning from our experiences.
Through self-reflection and introspection, we can uncover our strengths and weaknesses, and gain clarity on what truly matters to us.
This journey often involves stepping out of our comfort zones, facing challenges, and embracing change.
Self-discovery is not always easy, but it is essential for personal growth and fulfillment.
It''s a path that leads to greater self-awareness, confidence, and a deeper connection with ourselves and others.'
);

CREATE TABLE tags (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);


INSERT INTO tags (name) VALUES ('Wellness');
INSERT INTO tags (name) VALUES ('Productivity');
INSERT INTO tags (name) VALUES ('Mindfulness');
INSERT INTO tags (name) VALUES ('MorningRitual');
INSERT INTO tags (name) VALUES ('SelfCare');
INSERT INTO tags (name) VALUES ('Space');
INSERT INTO tags (name) VALUES ('Exploration');
INSERT INTO tags (name) VALUES ('Astronomy');
INSERT INTO tags (name) VALUES ('Science');
INSERT INTO tags (name) VALUES ('Technology');
INSERT INTO tags (name) VALUES ('Minimalism');
INSERT INTO tags (name) VALUES ('Lifestyle');
INSERT INTO tags (name) VALUES ('Simplicity');
INSERT INTO tags (name) VALUES ('SelfImprovement');
INSERT INTO tags (name) VALUES ('RenewableEnergy');
INSERT INTO tags (name) VALUES ('Sustainability');
INSERT INTO tags (name) VALUES ('Environment');
INSERT INTO tags (name) VALUES ('ClimateChange');
INSERT INTO tags (name) VALUES ('Coffee');
INSERT INTO tags (name) VALUES ('Beverage');
INSERT INTO tags (name) VALUES ('SolarPower');
INSERT INTO tags (name) VALUES ('Exercise');
INSERT INTO tags (name) VALUES ('Health');
INSERT INTO tags (name) VALUES ('Fitness');
INSERT INTO tags (name) VALUES ('MentalHealth');
INSERT INTO tags (name) VALUES ('Universe');
INSERT INTO tags (name) VALUES ('Cooking');
INSERT INTO tags (name) VALUES ('Food');
INSERT INTO tags (name) VALUES ('CulinaryArts');
INSERT INTO tags (name) VALUES ('Culture');
INSERT INTO tags (name) VALUES ('SelfDiscovery');
INSERT INTO tags (name) VALUES ('PersonalGrowth');





CREATE TABLE post_tags (
    post_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    FOREIGN KEY (post_id) REFERENCES posts(id),
    FOREIGN KEY (tag_id) REFERENCES tags(id),
    PRIMARY KEY (post_id, tag_id)
);

INSERT INTO post_tags (post_id, tag_id) VALUES (1, 1); 
INSERT INTO post_tags (post_id, tag_id) VALUES (3, 1); 
INSERT INTO post_tags (post_id, tag_id) VALUES (5, 1); 
INSERT INTO post_tags (post_id, tag_id) VALUES (7, 1); 
INSERT INTO post_tags (post_id, tag_id) VALUES (10, 1); 
INSERT INTO post_tags (post_id, tag_id) VALUES (1, 2); 
INSERT INTO post_tags (post_id, tag_id) VALUES (1, 3);
INSERT INTO post_tags (post_id, tag_id) VALUES (10, 3); 
INSERT INTO post_tags (post_id, tag_id) VALUES (1, 4); 
INSERT INTO post_tags (post_id, tag_id) VALUES (5, 4); 
INSERT INTO post_tags (post_id, tag_id) VALUES (1, 5); 
INSERT INTO post_tags (post_id, tag_id) VALUES (2, 6); 
INSERT INTO post_tags (post_id, tag_id) VALUES (8, 6); 
INSERT INTO post_tags (post_id, tag_id) VALUES (2, 7);
INSERT INTO post_tags (post_id, tag_id) VALUES (8, 7); 
INSERT INTO post_tags (post_id, tag_id) VALUES (2, 8);
INSERT INTO post_tags (post_id, tag_id) VALUES (8, 8); 
INSERT INTO post_tags (post_id, tag_id) VALUES (2, 9); 
INSERT INTO post_tags (post_id, tag_id) VALUES (8, 9); 
INSERT INTO post_tags (post_id, tag_id) VALUES (2, 10);
INSERT INTO post_tags (post_id, tag_id) VALUES (4, 10);
INSERT INTO post_tags (post_id, tag_id) VALUES (6, 10); 
INSERT INTO post_tags (post_id, tag_id) VALUES (3, 11); 
INSERT INTO post_tags (post_id, tag_id) VALUES (3, 12); 
INSERT INTO post_tags (post_id, tag_id) VALUES (5, 12);
INSERT INTO post_tags (post_id, tag_id) VALUES (9, 12);
INSERT INTO post_tags (post_id, tag_id) VALUES (10, 12); 
INSERT INTO post_tags (post_id, tag_id) VALUES (3, 13); 
INSERT INTO post_tags (post_id, tag_id) VALUES (3, 14); 
INSERT INTO post_tags (post_id, tag_id) VALUES (4, 15); 
INSERT INTO post_tags (post_id, tag_id) VALUES (6, 15); 
INSERT INTO post_tags (post_id, tag_id) VALUES (4, 16);
INSERT INTO post_tags (post_id, tag_id) VALUES (6, 16); 
INSERT INTO post_tags (post_id, tag_id) VALUES (4, 17);
INSERT INTO post_tags (post_id, tag_id) VALUES (6, 17); 
INSERT INTO post_tags (post_id, tag_id) VALUES (4, 18); 
INSERT INTO post_tags (post_id, tag_id) VALUES (5, 19); 
INSERT INTO post_tags (post_id, tag_id) VALUES (5, 20); 
INSERT INTO post_tags (post_id, tag_id) VALUES (6, 21); 
INSERT INTO post_tags (post_id, tag_id) VALUES (7, 22); 
INSERT INTO post_tags (post_id, tag_id) VALUES (7, 23); 
INSERT INTO post_tags (post_id, tag_id) VALUES (7, 24); 
INSERT INTO post_tags (post_id, tag_id) VALUES (7, 25); 
INSERT INTO post_tags (post_id, tag_id) VALUES (8, 26); 
INSERT INTO post_tags (post_id, tag_id) VALUES (9, 27); 
INSERT INTO post_tags (post_id, tag_id) VALUES (9, 28); 
INSERT INTO post_tags (post_id, tag_id) VALUES (9, 29); 
INSERT INTO post_tags (post_id, tag_id) VALUES (9, 30); 
INSERT INTO post_tags (post_id, tag_id) VALUES (10, 31);
INSERT INTO post_tags (post_id, tag_id) VALUES (10, 32);
