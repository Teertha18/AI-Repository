from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    def get_bigquery_usage(self):
        pass

    @abstractmethod
    def get_dataproc_usage(self):
        pass

    @abstractmethod
    def get_dataflow_usage(self):
        pass

    @abstractmethod
    def get_gcs_usage(self):
        pass