%global java_home %{_jvmlibdir}/java-1.8.0-openjdk

Name:           aopalliance
Version:        1.0
Release:        20%{?dist}
Summary:        Java/J2EE AOP standards
License:        Public Domain
URL:            http://aopalliance.sourceforge.net/
BuildArch:      noarch

# cvs -d:pserver:anonymous@aopalliance.cvs.sourceforge.net:/cvsroot/aopalliance login
# password empty
# cvs -z3 -d:pserver:anonymous@aopalliance.cvs.sourceforge.net:/cvsroot/aopalliance export -r HEAD aopalliance
Source0:        aopalliance-src.tar.gz
Source1:        http://repo1.maven.org/maven2/aopalliance/aopalliance/1.0/aopalliance-1.0.pom
Source2:        %{name}-MANIFEST.MF

BuildRequires:  ant
BuildRequires:  javapackages-local
BuildRequires:  java-1.8.0-openjdk-devel

%description
Aspect-Oriented Programming (AOP) offers a better solution to many
problems than do existing technologies, such as EJB.  AOP Alliance
intends to facilitate and standardize the use of AOP to enhance
existing middleware environments (such as J2EE), or development
environements (e.g. Eclipse).  The AOP Alliance also aims to ensure
interoperability between Java/J2EE AOP implementations to build a
larger AOP community.

%{?module_package}
%{?javadoc_package}

%prep
%setup -q -n %{name}

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant} -Dbuild.sysclasspath=only jar javadoc

# Inject OSGi manifest required by Eclipse.
jar umf %{SOURCE2} build/%{name}.jar

%install
%mvn_file : %{name}
%mvn_artifact %{SOURCE1} build/%{name}.jar

%mvn_install -J build/javadoc

%files -n %{?module_prefix}%{name} -f .mfiles

%changelog
* Sat Jan 25 2020 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-20
- Build with OpenJDK 8

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-19
- Mass rebuild for javapackages-tools 201902

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-18
- Mass rebuild for javapackages-tools 201901

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-16
- Switch to automatically-generated javadoc package

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 22 2017 Michael Simacek <msimacek@redhat.com> - 0:1.0-14
- Install with XMvn

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-11
- Add build-requires on javapackages-local

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.0-8
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 14 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-6
- Drop BR on zip, use jar instead
- Add more verbose description
- Update to current packaging guidelines

* Mon Feb 25 2013 Gerard Ryan <galileo.fedoraproject.org> 0:1.0-5
- Add OSGI manifest

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 20 2012 Tomas Radej <tradej@redhat.com> - 0:1.0-3
- Fixed tarball generation guide

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 6 2012 Andy Grimm <agrimm@gmail.com> 0:1.0-1
- build for Fedora
