from rest_framework import serializers
from schools.models import School,Location,SchoolImage

#LOCATION
class GetLocationSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Location
		fields = ('streetNum','streetName','apt','unit',
			'city','region','country','lattitude','longitude')

class GetLocationSuperUserSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Location

class PostLocationSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Location
		fields = ('schoolId','streetNum','streetName','apt','unit',
			'city','region','country','lattitude','longitude','toDelete')

#SCHOOL IMAGE
class GetSchoolImageSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = SchoolImage
		fields = ('id','imageLink','descriptor')

class GetSchoolImageSuperUserSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = SchoolImage
		fields = ('id','imageLink','descriptor')

class PostSchoolImageSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = SchoolImage

#SCHOOL
class GetSchoolSerializer(serializers.ModelSerializer):
	images = GetSchoolImageSerializer(many=True,required=False)
	location = GetLocationSerializer(required=False)
	
	class Meta:
		model = School
		fields = ('id','name','population','location','dateEstablished','numPrograms',
			'logoUrl','website','facebookLink','twitterLink','linkedinLink',
			'alumniNumber','totalFunding','images')

class GetSchoolSuperUserSerializer(serializers.ModelSerializer):
	images = GetSchoolImageSuperUserSerializer(many=True,required=False)
	location = GetLocationSuperUserSerializer(required=False)
	
	class Meta:
		model = School

class PostSchoolSerializer(serializers.ModelSerializer):
	class Meta:
		model = School
		fields = ('name','population','dateEstablished','numPrograms',
			'logoUrl','website','facebookLink','twitterLink','linkedinLink',
			'alumniNumber','totalFunding','toDelete')