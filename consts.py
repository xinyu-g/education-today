# data directory
DATA = './data/'

# mysql setup
HOST = 'localhost'
USER = 'root'
PASSWORD = 'root'
# DB = 'eductoday'
DB = 'edtoday'

# insert order
FILES = ["Affiliations", "Authors", "Papers", "PaperAuthorAffiliations", "PaperReferences"]
# FILES = ["PaperAuthorAffiliations", "PaperReferences"]

REDUCED_SCHEMA = {
    "Affiliations": {
        "cols": [
            "AffiliationId",
            "Rank",
            "NormalizedName",
            "DisplayName",
            # "GridId",
            # "OfficialPage",
            # "WikiPage",
            "PaperCount",
            # "PaperFamilyCount",
            # "CitationCount",
            # "Iso3166Code",
            # "Latitude",
            # "Longitude",
            # "CreatedDate"
        ],
        "size": 1000000
    },
    "PaperAuthorAffiliations": {
        "cols": [
            "PaperId",
            "AuthorId",
            "AffiliationId",
            # "AuthorSequenceNumber",
            # "OriginalAuthor",
            # "OriginalAffiliation"
        ],
        "size": 1000000
    },
    "Authors": {
        "cols": [
            "AuthorId",
            "Rank",
            "NormalizedName",
            "DisplayName",
            "LastKnownAffiliationId",
            "PaperCount",
            # "PaperFamilyCount",
            # "CitationCount",
            # "CreatedDate"
        ],
        "size": 1000000
    },
    "PaperReferences": {
        "cols": [
            "PaperId",
            "PaperReferenceId"
        ],
        "size": 1000000
    },
    "Papers": {
        "cols": [
            "PaperId",
            "Rank",
            # "Doi",
            # "DocType",
            # "PaperTitle",
            # "OriginalTitle",
            # "BookTitle",
            # "Year",
            # "Date",
            # "OnlineDate",
            # "Publisher",
            # "JournalId",
            # "ConferenceSeriesId",
            # "ConferenceInstanceId",
            # "Volume",
            # "Issue",
            # "FirstPage",
            # "LastPage",
            "ReferenceCount",
            "CitationCount",
            "EstimatedCitation",
            # "OriginalVenue",
            # "FamilyId",
            # "FamilyRank",
            # "DocSubTypes",
            # "CreatedDate"
        ],
        "size": 50000
    }
}

SCHEMA = {
    "Affiliations": {
        "cols": [
            "AffiliationId",
            "Rank",
            "NormalizedName",
            "DisplayName",
            "GridId",
            "OfficialPage",
            "WikiPage",
            "PaperCount",
            "PaperFamilyCount",
            "CitationCount",
            "Iso3166Code",
            "Latitude",
            "Longitude",
            "CreatedDate"
        ],
        "idx": ["AffiliationId"],
        "size": 1000000
    },
    "PaperAuthorAffiliations": {
        "cols": [
            "PaperId",
            "AuthorId",
            "AffiliationId",
            "AuthorSequenceNumber",
            "OriginalAuthor",
            "OriginalAffiliation"
        ],
        "idx": [],
        "size": 1000000
    },
    "Authors": {
        "cols": [
            "AuthorId",
            "Rank",
            "NormalizedName",
            "DisplayName",
            "LastKnownAffiliationId",
            "PaperCount",
            "PaperFamilyCount",
            "CitationCount",
            "CreatedDate"
        ],
        "idx": ["AuthorId"],
        "size": 1000000
    },
    "PaperReferences": {
        "cols": [
            "PaperId",
            "PaperReferenceId"
        ],
        "idx": [
            "PaperId", 
            "PaperReferenceId"
        ],
        "size": 1000000
    },
    "Papers": {
        "cols": [
            "PaperId",
            "Rank",
            "Doi",
            "DocType",
            "PaperTitle",
            "OriginalTitle",
            "BookTitle",
            "Year",
            "Date",
            "OnlineDate",
            "Publisher",
            "JournalId",
            "ConferenceSeriesId",
            "ConferenceInstanceId",
            "Volume",
            "Issue",
            "FirstPage",
            "LastPage",
            "ReferenceCount",
            "CitationCount",
            "EstimatedCitation",
            "OriginalVenue",
            "FamilyId",
            "FamilyRank",
            # "DocSubTypes",
            "CreatedDate"
        ],
        "idx": ["PaperId"],
        "size": 50000
    }
}