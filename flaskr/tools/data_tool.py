import os
import pandas as pd
import pickle
import numpy as np

rootPath = os.path.abspath(os.getcwd())


def load_data():
    return getCourses(), getCategories(), getSubCategories(), getPriceRanges(), getNumLecturesRanges(), getContentLengthMinutesRanges()


def getCourses():
    rootPath = os.path.abspath(os.getcwd())
    path = f"{rootPath}/data/processed/course_info_minified.pkl"
    df = pd.read_pickle(path)
    df = df.sample(frac=1).reset_index(drop=True)
    df.set_index('id')
    return df

def getCategories():
    rootPath = os.path.abspath(os.getcwd())
    path = f"{rootPath}/data/processed/category.pkl"
    with open(path, 'rb') as f:
        categories = pickle.load(f)
    categories_df = pd.DataFrame(categories)
    categories_df.set_index('id')
    return categories_df

def getSubCategories():
    rootPath = os.path.abspath(os.getcwd())
    path = f"{rootPath}/data/processed/subcategory.pkl"
    with open(path, 'rb') as f:
        subcategories = pickle.load(f)
    subcategories_df = pd.DataFrame(subcategories)
    subcategories_df.set_index('id')
    return subcategories_df

def getPriceRanges():
    rootPath = os.path.abspath(os.getcwd())
    path = f"{rootPath}/data/processed/id2price.pkl"
    with open(path, 'rb') as f:
        price = pickle.load(f)
    price_df = pd.DataFrame(price)
    price_df.set_index('id')
    return price_df


def getNumLecturesRanges():
    rootPath = os.path.abspath(os.getcwd())
    path = f"{rootPath}/data/processed/id2num_lectures.pkl"
    with open(path, 'rb') as f:
        num_lectures = pickle.load(f)
    num_lectures_df = pd.DataFrame(num_lectures)
    num_lectures_df.set_index('id')
    return num_lectures_df


def getContentLengthMinutesRanges():
    rootPath = os.path.abspath(os.getcwd())
    path = f"{rootPath}/data/processed/id2content_length_min.pkl"
    with open(path, 'rb') as f:
        content_length_min = pickle.load(f)
    content_length_min_df = pd.DataFrame(content_length_min)
    content_length_min_df.set_index('id')
    return content_length_min_df


def get_category_similarity_matrix():
    category_similarity_matrix = np.load(
        f'{rootPath}/data/processed/category_similarity_matrix.npy')
    return category_similarity_matrix


def get_subcategory_similarity_matrix():
    subcategory_similarity_matrix = np.load(
        f'{rootPath}/data/processed/subcategory_similarity_matrix.npy')
    return subcategory_similarity_matrix


def get_price_bin2vec():
    with open(f'{rootPath}/data/processed/bins2price.pkl', 'rb') as f:
        price_bin2vec = pickle.load(f)
    return price_bin2vec


def get_num_lectures_bin2vec():
    with open(f'{rootPath}/data/processed/bins2num_lectures.pkl', 'rb') as f:
        num_lectures_bin2vec = pickle.load(f)
    return num_lectures_bin2vec


def get_content_length_minutes_bin2vec():
    with open(f'{rootPath}/data/processed/bins2content_length_min.pkl', 'rb') as f:
        content_length_minutes_bin2vec = pickle.load(f)
    return content_length_minutes_bin2vec

# user id | item id | rating | timestamp


def getRates():
    rootPath = os.path.abspath(os.getcwd())
    path = f"{rootPath}/flaskr/static/ml_data_lab2/ratings.csv"
    df = pd.read_csv(path, delimiter=",", names=[
                     "userId", "courseId", "rating", "timestamp"])
    df = df.drop(columns='timestamp')
    df = df[['userId', 'courseId', 'rating']]

    return df


# itemID | userID | rating
def ratesFromUser(rates):
    itemID = []
    userID = []
    rating = []

    for rate in rates:
        items = rate.split("|")
        userID.append(int(items[0]))
        itemID.append(int(items[1]))
        rating.append(int(items[2]))

    ratings_dict = {
        "userId": userID,
        "id": itemID,
        "rating": rating,
    }

    return pd.DataFrame(ratings_dict)
