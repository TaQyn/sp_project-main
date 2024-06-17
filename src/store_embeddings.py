from face_embeddings.Extract_Embeddings.embeddingextractor import EmbeddingExtractor
from face_embeddings.Store_Embeddings.faissindex import FaissIndex


def store_embeddings(dataset_path, model_name):
    extractor = EmbeddingExtractor(dataset_path, model_name)
    embeddings, labels = extractor.extract_embeddings()
    faiss_index = FaissIndex(embeddings, labels)
    faiss_index.save_index(
        r"C:\Users\nguye\Downloads\Doan\sp_project-main\sp_project-main\src\face_embeddings\weights\faiss_index.bin",
        r"C:\Users\nguye\Downloads\Doan\sp_project-main\sp_project-main\src\face_embeddings\weights\labels.txt",
    )


if __name__ == "__main__":
    dataset_path = r"C:\Users\nguye\Downloads\Doan\sp_project-main\sp_project-main\src\dataset"
    model_name = "OpenFace"
    store_embeddings(dataset_path, model_name)
