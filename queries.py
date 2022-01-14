

CREATE_TABLES = (
    """
    CREATE DATABASE IF NOT EXISTS eductoday
    """,
    """
    USE eductoday
    """,
    """
    CREATE TABLE IF NOT EXISTS Affiliations (
        AffiliationId BIGINT,
        `Rank` INT UNSIGNED,
        NormalizedName TEXT,
        DisplayName TEXT,
        GridId TEXT,
        OfficialPage TEXT,
        WikiPage TEXT,
        PaperCount BIGINT,
        PaperFamilyCount BIGINT,
        CitationCount BIGINT,
        Iso3166Code TEXT,
        Latitude FLOAT,
        Longitude FLOAT,
        CreatedDate DATETIME,
        PRIMARY KEY (AffiliationId)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Authors (
        AuthorId BIGINT,
        `Rank` INT UNSIGNED,
        NormalizedName TEXT,
        DisplayName TEXT,
        LastKnownAffiliationId BIGINT,
        PaperCount BIGINT,
        PaperFamilyCount BIGINT,
        CitationCount BIGINT,
        CreatedDate DATETIME,
        PRIMARY KEY (AuthorId)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Papers (
        PaperId BIGINT,
        `Rank` INT UNSIGNED,
        Doi TEXT,
        DocType TEXT,
        PaperTitle TEXT,
        OriginalTitle TEXT,
        BookTitle TEXT,
        Year BIGINT,
        Date DATETIME,
        OnlineDate DATETIME, 
        Publisher TEXT,
        JournalId BIGINT,
        ConferenceSeriesId BIGINT,
        ConferenceInstanceId BIGINT,
        Volume TEXT,
        Issue TEXT,
        FirstPage TEXT,
        LastPage TEXT,
        ReferenceCount BIGINT,
        CitationCount BIGINT,
        EstimatedCitation BIGINT,
        OriginalVenue TEXT,
        FamilyId BIGINT,
        FamilyRank INT UNSIGNED,
        DocSubTypes TEXT,
        CreatedDate DATETIME,
        PRIMARY KEY (PaperId)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS PaperAuthorAffiliations (
        PaperId BIGINT,
        AuthorId BIGINT,
        AffiliationId BIGINT,
        AuthorSequenceNumber INT UNSIGNED,
        OriginalAuthor TEXT,
        OriginalAffiliation TEXT
    )
    """,
        # FOREIGN KEY (PaperId) REFERENCES Papers(PaperId)
        #     ON DELETE CASCADE,
        # FOREIGN KEY (AuthorId) REFERENCES Authors(AuthorId)
        #     ON DELETE CASCADE,
        # FOREIGN KEY (AffiliationId) REFERENCES Affiliations(AffiliationId)
        #     ON DELETE CASCADE
    """
    CREATE TABLE IF NOT EXISTS PaperReferences (
        PaperId BIGINT,
        PaperReferenceId BIGINT,
        PRIMARY KEY (PaperId, PaperReferenceId)
    )
    """
    # FOREIGN KEY (PaperId) REFERENCES Papers(PaperId)
    #     ON DELETE CASCADE,
    # FOREIGN KEY (PaperReferenceId) REFERENCES Papers(PaperId)
    #     ON DELETE CASCADE
)