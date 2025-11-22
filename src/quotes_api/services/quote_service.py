"""
Quote business logic service.
"""

import random
from typing import List, Optional

from quotes_api.models.quote import Quote


class QuoteService:
    """Service for managing quotes."""

    def __init__(self):
        """Initialize the quote service."""
        # Sample quotes database
        self._quotes = [
            Quote(
                id=1,
                text="La vie est une fleur dont l'amour est le miel.",
                author="Victor Hugo",
                category="Amour",
                language="fr"
            ),
            Quote(
                id=2,
                text="Le succès n'est pas la clé du bonheur. Le bonheur est la clé du succès.",
                author="Albert Schweitzer",
                category="Succès",
                language="fr"
            ),
            Quote(
                id=3,
                text="La seule façon de faire un travail formidable est d'aimer ce que vous faites.",
                author="Steve Jobs",
                category="Travail",
                language="fr"
            ),
            Quote(
                id=4,
                text="L'avenir appartient à ceux qui croient à la beauté de leurs rêves.",
                author="Eleanor Roosevelt",
                category="Rêves",
                language="fr"
            ),
            Quote(
                id=5,
                text="La seule vraie sagesse est de savoir que l'on ne sait rien.",
                author="Socrate",
                category="Sagesse",
                language="fr"
            ),
            Quote(
                id=6,
                text="La vie est trop courte pour boire du mauvais vin.",
                author="Proverbe français",
                category="Plaisir",
                language="fr"
            ),
            Quote(
                id=7,
                text="Dans la vie, il n'y a pas de solutions. Il y a des forces en marche.",
                author="Albert Camus",
                category="Philosophie",
                language="fr"
            ),
            Quote(
                id=8,
                text="L'homme n'est rien d'autre que ce qu'il fait de lui-même.",
                author="Jean-Paul Sartre",
                category="Existentialisme",
                language="fr"
            ),
            Quote(
                id=9,
                text="La liberté consiste à pouvoir faire tout ce qui ne nuit pas à autrui.",
                author="Déclaration des Droits de l'Homme",
                category="Liberté",
                language="fr"
            ),
            Quote(
                id=10,
                text="L'imagination est plus importante que le savoir.",
                author="Albert Einstein",
                category="Créativité",
                language="fr"
            )
        ]

    def get_random_quote(self) -> Quote:
        """Get a random quote."""
        return random.choice(self._quotes)

    def get_quote_by_id(self, quote_id: int) -> Optional[Quote]:
        """Get a quote by its ID."""
        return next((quote for quote in self._quotes if quote.id == quote_id), None)

    def get_all_quotes(self) -> List[Quote]:
        """Get all quotes."""
        return self._quotes.copy()

    def get_quotes_by_category(self, category: str) -> List[Quote]:
        """Get quotes by category."""
        return [quote for quote in self._quotes if quote.category and quote.category.lower() == category.lower()]

    def get_quotes_by_author(self, author: str) -> List[Quote]:
        """Get quotes by author."""
        return [quote for quote in self._quotes if quote.author and quote.author.lower() == author.lower()]

    def search_quotes(self, query: str) -> List[Quote]:
        """Search quotes by text content."""
        query_lower = query.lower()
        return [
            quote for quote in self._quotes
            if query_lower in quote.text.lower() or
            (quote.author and query_lower in quote.author.lower()) or
            (quote.category and query_lower in quote.category.lower())
        ]

    def get_categories(self) -> List[str]:
        """Get all unique categories."""
        categories = {quote.category for quote in self._quotes if quote.category}
        return sorted(list(categories))

    def get_authors(self) -> List[str]:
        """Get all unique authors."""
        authors = {quote.author for quote in self._quotes if quote.author}
        return sorted(list(authors))